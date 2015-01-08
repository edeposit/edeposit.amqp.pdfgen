#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from base64 import b64encode
from collections import namedtuple


# Functions & classes =========================================================
def pdf_from_file(file_obj):
    return PDF(
        b64encode(file_obj.read())
    )


class PDF(namedtuple("PDF", ["b64_content"])):
    pass
