LATEX       = pdflatex
BASH        = bash -c
ECHO        = echo
RM          = rm -rf
RM_TMP      = ${RM} $(foreach suff, ${TMP_SUFFS}, ${NAME}.${suff})

TMP_SUFFS   = pdf aux bbl blg log dvi ps eps
SUFF        = pdf

CHECK_RERUN = grep Rerun ${NAME}.log

DOC_OUT = ${NAME}.${SUFF}

default: ${DOC_OUT}

${DOC_OUT}: ${NAME}.tex ${NAME}.bib
	pdflatex ${NAME}
	bibtex ${NAME}
	pdflatex ${NAME}
	pdflatex ${NAME}

clean:
	${RM_TMP}
