#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os.path
from StringIO import StringIO
from string import Template

from rst2pdf.createpdf import RstToPdf


# Functions & classes =========================================================
def _resource_context(fn):
    """
    Compose path to the ``resources`` directory for given `fn`.

    Args:
        fn (str): Filename of file in ``resources`` directory.

    Returns:
        str: Absolute path to the file in resources directory.
    """
    return os.path.join(
        os.path.dirname(__file__),
        "resources",
        fn
    )


def _init_pdf():
    """
    Initialize :class:`RstToPdf` class.

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
            _resource_context("style.json")
        ],
        breaklevel=0,
        splittables=True,
        footer="###Page###/###Total###"
    )


def get_contract(firma, pravni_forma, sidlo, ic, dic, zastoupen, jednajici):
    """
    Compose contract and create PDF.

    Args:
        firma (str): firma
        pravni_forma (str): pravni_forma
        sidlo (str): sidlo
        ic (str): ic
        dic (str): dic
        zastoupen (str): zastoupen
        jednajici (str): jednajici

    Returns:
        obj: StringIO file instance containing PDF file.
    """
    contract_fn = _resource_context(
        "Licencni_smlouva_o_dodavani_elektronickych_publikaci"
        "_a_jejich_uziti.rst"
    )

    # load contract
    with open(contract_fn) as f:
        contract = f.read()

    # make sure that `firma` has its heading mark
    firma = firma.strip()
    firma = firma + ":\n" + (len(firma) * "-")

    # patch template
    contract = Template(contract).substitute(
        firma=firma,
        pravni_forma=pravni_forma.strip(),
        sidlo=sidlo.strip(),
        ic=ic.strip(),
        dic=dic.strip(),
        zastoupen=zastoupen.strip(),
        jednajici=jednajici.strip(),
    )

    pdf = _init_pdf()
    out_file_obj = StringIO()

    # create PDF
    pdf.createPdf(
        text=contract,
        output=out_file_obj
    )

    # rewind file pointer to begin
    out_file_obj.seek(0)

    return out_file_obj
