#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from StringIO import StringIO
from tempfile import NamedTemporaryFile

from rst2pdf.createpdf import RstToPdf


# Functions & classes =========================================================
def _init_pdf(style_path, header=None, footer="###Page###/###Total###"):
    """
    Initialize :class:`RstToPdf` class.

    Args:
        style_path (str): Path to the style for the PDF.

    Returns:
        obj: Initialized object.
    """
    return RstToPdf(
        language="cs",
        font_path=[
            "/usr/share/fonts",
            '.',
            '/usr/local/lib/python2.7/dist-packages/rst2pdf/fonts'
        ],
        stylesheets=[
            style_path
        ],
        breaklevel=0,
        splittables=True,
        header=header,
        footer=footer
    )


def gen_pdf(content, style_text, header=None, footer="###Page###/###Total###"):
    out_file_obj = StringIO()

    with NamedTemporaryFile() as f:
        f.write(style_text)
        f.flush()

        pdf = _init_pdf(f.name, header, footer)

    # create PDF
    pdf.createPdf(text=content, output=out_file_obj)

    # rewind file pointer to begin
    out_file_obj.seek(0)

    return out_file_obj
