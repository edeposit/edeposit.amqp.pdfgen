#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os
import os.path
import filecmp
from StringIO import StringIO
from tempfile import NamedTemporaryFile

from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

import translator


# Variables ===================================================================
filename = None


# Tests =======================================================================
def get_pdf_content(fp):
    out = StringIO()
    rsrcmgr = PDFResourceManager(caching=False)
    laparams = LAParams()
    device = TextConverter(
        rsrcmgr,
        out,
        codec='utf-8',
        laparams=laparams,
    )

    interpreter = PDFPageInterpreter(rsrcmgr, device)

    maxpages = 0
    password = ''
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password, caching=False,
                                  check_extractable=True):
        interpreter.process_page(page)

    out.seek(0)
    return out.read()


def test_translator():
    obj = translator.get_contract(
        "Franta Putšálek",
        "Nope",
        "Praha",
        "27827272",
        "73646723",
        "Ne",
        "Nekdo"
    )

    with NamedTemporaryFile(delete=False) as f:
        f.write(obj.read())

        global filename
        filename = f.name

    example_fn = os.path.join(os.path.dirname(__file__), "example.pdf")

    ex_content = get_pdf_content(open(example_fn))
    tmp_content = get_pdf_content(open(filename))

    assert ex_content == tmp_content


def teardown_module():
    os.unlink(filename)
