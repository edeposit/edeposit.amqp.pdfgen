#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from rst2pdf.createpdf import RstToPdf



# Variables ===================================================================



# Functions & classes =========================================================



# Main program ================================================================
pdf = RstToPdf(
    language="cs",
    font_path=[
        "/usr/share/fonts",
        '.',
        '/usr/local/lib/python2.7/dist-packages/rst2pdf/fonts'
    ],
    stylesheets=["style.json"],
    breaklevel=0,
    splittables=True,
    footer="###Page###/###Total###"
)
pdf.createPdf(
    text=open("contract.rst").read(),
    output='foo.pdf'
)