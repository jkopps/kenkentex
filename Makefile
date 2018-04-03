all: final_guestpuzzles.pdf

final_guestpuzzles.pdf: guestpuzzles.tex
	pdflatex guestpuzzles.tex && pdflatex guestpuzzles.tex && \
	pdflatex flip.tex && pdflatex flip.tex && \
	pdflatex join.tex && pdflatex join.tex && \
	cp join.pdf final_guestpuzzles.pdf

guestpuzzles.tex: assignments.csv
	python genguestcards.py > guestpuzzles.tex
