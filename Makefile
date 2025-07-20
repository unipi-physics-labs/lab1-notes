all: pdf

armageddon: snippets figs statnotes compnotes exercises

latest: statnotes compnotes exercises

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

exercises:
	pdflatex exercises
	pdflatex exercises

snips:
	python tools/py2tex.py snippy

figs:
	python macro/plot_all.py

sanitize:
	python tools/sanitize.py chapters
	python tools/sanitize.py misc/colophon.tex
	python tools/sanitize.py misc/credits.tex
	python tools/sanitize.py misc/prefazione.tex

doc:
	cd docs; make html; cd -

cleandoc:
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

cleanall: clean cleandoc
	rm -f statnotes.pdf
