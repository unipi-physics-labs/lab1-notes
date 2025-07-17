all:
	pdflatex statnotes
	bibtex statnotes
	pdflatex statnotes
	pdflatex statnotes

pdf:
	pdflatex statnotes

snippets:
	python tools/py2tex.py snippy

docshtml:
	cd docs; make html; cd -

docsclean:
	cd docs; make clean; cd -

flake:
	flake8 tools --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics

ruff:
	ruff check tools

lint:
	pylint tools

clean:
	rm -f *.aux *.log *~ *.mtc* *.idx *.out *.toc *.maf *.fls *.fdb_latexmk *.ilg *.ind *.synctex*
	cd chapters; rm -f *~ *.aux *.log *.bbl *.blg; cd -
	rm -f misc/*~ misc/*.aux
	rm -f statnotes.bbl statnotes.blg

cleanall:
	make clean; rm -f statnotes.pdf
