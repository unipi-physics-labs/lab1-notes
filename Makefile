all:
	pdflatex statnotes
	bibtex statnotes
	pdflatex statnotes
	pdflatex statnotes

pdf:
	pdflatex statnotes


docshtml:
	cd docs; make html; cd -

docsclean:
	cd docs; make clean; cd -

clean:
	rm -f *.aux *.log *~ *.mtc* *.idx *.out *.toc *.maf *.fls *.fdb_latexmk *.ilg *.ind *.synctex*
	cd chapters; rm -f *~ *.aux *.log *.bbl *.blg; cd -
	rm -f misc/*~ misc/*.aux
	rm -f statnotes.bbl statnotes.blg

cleanall:
	make clean; rm -f statnotes.pdf
