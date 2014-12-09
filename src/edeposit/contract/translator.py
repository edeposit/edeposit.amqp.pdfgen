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
    return os.path.join(
        os.path.dirname(__file__),
        "resources",
        fn
    )


def _init_pdf():
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

obj = get_contract(
    "Franta Putšálek",
    "Nope",
    "Praha",
    "27827272",
    "73646723",
    "Ne",
    "Nekdo"
)

with open("test.pdf", "wb") as f:
    f.write(obj.read())