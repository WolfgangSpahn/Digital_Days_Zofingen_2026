help:                 ## Show this help.
	@grep -F -h "##" $(MAKEFILE_LIST) | grep -F -v grep | sed -e "s/\\$$//" | sed -e "s/##//"

SERVER ?= fra-server
DOCS_PATH ?=atelier3
ATELIERS_DIR ?= $(CURDIR)
ATELIER_NUMBER = $(patsubst atelier%,%,$(DOCS_PATH))
ATELIER_LABEL = ATELIER $(ATELIER_NUMBER)
PRESENTER ?= $(if $(filter atelier1,$(DOCS_PATH)),Marc,$(if $(filter atelier2,$(DOCS_PATH)),Wolfgang,$(if $(filter atelier3,$(DOCS_PATH)),Philipp,)))
VOUCHER ?= aidu_wolfsclass_863f0bff

#-------

FIND=find
# use env var PRESENTAION_NAME=presentation
NAME=$(DOCS_PATH)_Digital_Days_Zofingen_2026
QMD=index.qmd

PORT=5050

# sources
IMG_DIR_ORIG=$(HOME)/Projects/wsp-images/

# targets
IMG_DIR = $(DOCS_PATH)/images
DOCS_TAR_PATH=$(NAME).tar.gz
REMOTE_PATH=~/
SERV_PREFIX=/usr/share/nginx/
LOC_PREFIX=/usr/share/nginx/
INTERAKTIV=html/interaktiv/


# quarto paths
QUARTO_PRJ=$(HOME)/Projects/Quarto
QUARTO_FRONTEND_DIR=$(QUARTO_PRJ)/interaktiv-frontend/
QUARTO_BACKEND_DIR=$(QUARTO_PRJ)/interaktiv-backend/
QUARTO_FRONTEND_BUNDLE=$(QUARTO_FRONTEND_DIR)built/index.js

# Embedded applet build paths
APPLET_BUILD_AN_ATOM_DIR ?= $(HOME)/Projects/Solidjs/applet-build-an-atom

#-------
.PHONY: local.ateliers render images serve upload upload.ateliers load load.ateliers interaktive.run dev docs links literatur

literatur:            ## create a link to the literature.bib file
	ln -s ~/Projects/ai-tutoring-literature/literature.bib literature.bib

render:               ## Render the markdown with quarto into DOCS_PATH
	sed 's/atelier/$(DOCS_PATH)/g' includes.orig.html > includes.html
	cat includes.html
	@mkdir -p $(DOCS_PATH)/images
	@cp -rf images/icons $(DOCS_PATH)/images/
	@npm --prefix "$(APPLET_BUILD_AN_ATOM_DIR)" run build-app
	@ATELIER_LABEL="$(ATELIER_LABEL)" PRESENTER="$(PRESENTER)" VOUCHER="$(VOUCHER)" quarto render $(QMD) --output-dir $(DOCS_PATH)/
	@mkdir -p $(DOCS_PATH)/site_libs/applet-build-an-atom
	@cp -rf "$(APPLET_BUILD_AN_ATOM_DIR)/dist/." $(DOCS_PATH)/site_libs/applet-build-an-atom/

images:               ## Create a symbolic link to the images directory
	ln -s $(IMG_DIR_ORIG) images

links:               ## Create symbolic links for `lit` and `images` from $HOME
	@echo "Creating symlink for lit -> $(HOME)/Projects/ai-tutoring-literature"
	@ln -sfn $(HOME)/Projects/ai-tutoring-literature lit
	@echo "Creating symlink for images -> $(IMG_DIR_ORIG)"
	@ln -sfn $(IMG_DIR_ORIG) images

serve:                ## Serves the project via quarto
serve: render
	quarto preview

upload:               ## Upload the DOCS_PATH and frontend js to the server
upload: render
	tar -cvzf $(DOCS_TAR_PATH) $(DOCS_PATH)/ && \
	scp -r $(DOCS_TAR_PATH) $(SERVER):$(REMOTE_PATH) && \
	ssh $(SERVER) "rm -rf $(SERV_PREFIX)$(INTERAKTIV)$(DOCS_PATH)/" && \
	ssh $(SERVER) "tar -xvf $(REMOTE_PATH)$(DOCS_TAR_PATH) -C $(SERV_PREFIX)$(INTERAKTIV)"
	@echo "index.js are uploaded via the interaktiv-frontend project in $(QUARTO_FRONTEND_DIR)."

upload.ateliers:      ## Upload all three atelier presentations to the server.
	@for session in atelier1 atelier2 atelier3; do \
		case "$$session" in \
			atelier1) atelier_number=1; presenter="Marc"; voucher="aidu_marcsclass_b002371c" ;; \
			atelier2) atelier_number=2; presenter="Wolfgang"; voucher="aidu_wolfsclass_863f0bff" ;; \
			atelier3) atelier_number=3; presenter="Philipp"; voucher="aidu_philippsclass_3c066dfe" ;; \
			*) echo "Unknown atelier session: $$session"; exit 1 ;; \
		esac; \
		$(MAKE) -C "$(ATELIERS_DIR)" upload \
			DOCS_PATH=$$session \
			ATELIER_NUMBER=$$atelier_number \
			PRESENTER="$$presenter" \
			VOUCHER="$$voucher" || exit 1; \
	done

load:                 ## Load DOCS_PATH and frontend js to local nginx server
load: render
	echo "Loading $(DOCS_PATH)/ and frontend js to local nginx server..."
	mkdir -p $(LOC_PREFIX)$(INTERAKTIV)$(DOCS_PATH)/
	cp -r $(DOCS_PATH)/* $(LOC_PREFIX)$(INTERAKTIV)$(DOCS_PATH)/
	@echo "index.js are uploaded via the interaktiv-frontend project  in $(QUARTO_FRONTEND_DIR)."


interaktive.run:      ## Run the interactive backend server
	cd $(QUARTO_BACKEND_DIR) && make run

dev:                  ## Serves the project in development mode from $(DOCS_TAR_PATH) using Python's http.server
	@echo "🔍 Checking if port $(PORT) is in use..."
	@if ss -lnt | grep -q ":$(PORT) "; then \
		echo "❌ Port $(PORT) is already in use. Maybe Docker or another process is running."; \
		echo "❌ Properly we are using nginx as a local server, please stop it or change the port."; \
	else \
		echo "✅ Port $(PORT) is free. Starting development server..."; \
		cd $(DOCS_TAR_PATH) && python -m http.server $(PORT); \
	fi

docs:                 ## Copy DOCS_PATH to docs for github pages
	rm -rf docs/
	mkdir -p docs/interaktiv/
	cp -r $(DOCS_PATH)/* docs/
	cp $(QUARTO_FRONTEND_BUNDLE) docs/interaktiv/index.js
	sed -i 's|import "/interaktiv/index.js"|import "./interaktiv/index.js"|' docs/index.html

clean:                ## clean up
	rm -rf $(DOCS_PATH)
	rm -rf .quarto
	rm -rf node_modules
	find . -type f -name '*~' -delete

docker.clean:         ## Clean up Docker containers, images, and volumes
	docker stop $(docker ps -aq) 2>/dev/null || true
	docker rm -f $(docker ps -aq) 2>/dev/null || true
	docker rmi -f $(docker images -aq) 2>/dev/null || true
	docker volume rm $(docker volume ls -q) 2>/dev/null || true
	docker system prune -f
	docker system prune -a --volumes -f
	@echo "Docker cleanup completed."
