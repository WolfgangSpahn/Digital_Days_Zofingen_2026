help:        ## Show this help.
	@grep -F "##" $(MAKEFILE_LIST) | grep -v "grep" | sed -e "s/\\$$//" -e "s/##//"

# Define source and target patterns
MD_FILES := $(wildcard *.md)
PDF_FILES := $(MD_FILES:.md=.pdf)


# PDF generation rule
pdf: $(PDF_FILES)  ## Create PDFs from MD files via Pandoc

# Pattern rule to convert each MD file to a PDF
%.pdf: %.md
	@echo "Converting $< to $@"
	pandoc $< -o $@ --pdf-engine=xelatex -f markdown+tex_math_single_backslash --highlight-style=custom.theme

clean:  ## Remove generated PDF files
	rm -f $(PDF_FILES)