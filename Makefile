all: pdf

armageddon: snippets pdf

pdf:
	pdflatex statnotes
	bibtex statnotes
	pdflatex statnotes
	pdflatex statnotes

fast:
	pdflatex statnotes

snippets:
	python tools/py2tex.py snippy

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
	flake8 tools --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics

ruff:
	ruff check tools

pylint:
	pylint tools

clean:
	rm -f *.aux *.log *~ *.mtc* *.idx *.out *.toc *.maf *.fls *.fdb_latexmk *.ilg *.ind *.synctex*
	cd chapters; rm -f *~ *.aux *.log *.bbl *.blg; cd -
	rm -f misc/*~ misc/*.aux
	rm -f statnotes.bbl statnotes.blg

cleanall: clean cleandocs
	rm -f statnotes.pdf
