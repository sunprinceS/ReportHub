SRC = main.tex
CACHE_DIR = tmp
PDF = $(notdir $(CURDIR)).pdf
#COMPILE_TEX := latexmk -xelatex -output-directory=$(CACHE_DIR)

.PHONY: pdf clean

pdf: $(SRC) | clean $(CACHE_DIR)
	#@$(COMPILE_TEX)
	#@mv $(CACHE_DIR)/main.pdf $(PDF)

$(CACHE_DIR):
	@mkdir -p $(CACHE_DIR)

clean:
	latexmk -CA $(JOBNAME).fdb_latexmk
	#@rm -f $(PDF)
	#@rm -rf $(CACHE_DIR)
