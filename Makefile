all: pdf

armageddon: snippets figs statnotes compnotes

statnotes:
	pdflatex statnotes
	bibtex statnotes
	pdflatex statnotes
	pdflatex statnotes

compnotes:
	pdflatex compnotes
	bibtex compnotes
	pdflatex compnotes
	pdflatex compnotes

snips:
	python tools/py2tex.py snippy

figs:
	python macro/plot_all.py

sanitize:
	python tools/sanitize.py chapters
	python tools/sanitize.py misc/colophon.tex
	python tools/sanitize.py misc/credits.tex
	python tools/sanitize.py misc/prefazione.tex

docs:
	cd docs; make html; cd -

cleandocs:
	cd docs; make clean; cd -

flake:
	flake8 tools --count --exit-zero --max-complexity=11 --max-line-length=100 --statistics

ruff:
	ruff check tools

lint:
	pylint tools

clean:
	rm -f *.aux *.log *~ *.mtc* *.idx *.out *.toc *.maf *.fls *.fdb_latexmk *.ilg *.ind *.synctex*
	rm -f *.bbl *.blg *.pdf
	cd chapters; rm -f *~ *.aux *.log *.bbl *.blg; cd -
	rm -f misc/*~ misc/*.aux

cleanall: clean cleandocs
	rm -f statnotes.pdf
