all:
	pdflatex guestpuzzles.tex && pdflatex guestpuzzles.tex && \
	pdflatex flip.tex && pdflatex flip.tex && \
	pdflatex join.tex && pdflatex join.tex && \
	cp join.pdf guestpuzzles_final.pdf
