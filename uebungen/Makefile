help:        ## Show this help.
	@grep -F "##" $(MAKEFILE_LIST) | grep -v "grep" | sed -e "s/\\$$//" -e "s/##//"

HTML_FILES := 


compress:    ## Compress all PDF files in the current directory and its subdirectories into a single gzipped tarball.
	find . \( -name "*.pdf" -o -name "applet*.html" \)  -print0 | tar --null -cvf uebungen.tar --files-from=- | gzip > uebungen.tar.gz
