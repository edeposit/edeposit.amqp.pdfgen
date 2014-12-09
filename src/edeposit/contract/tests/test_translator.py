#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os
import os.path
import filecmp
from tempfile import NamedTemporaryFile

import translator


filename = None

# Tests =======================================================================
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
        f.flush()

        global filename
        filename = f.name

        assert filecmp.cmp(
            f.name,
            os.path.join(
                os.path.dirname(__file__),
                "example.pdf"
            )
        )

def teardown_module():
    os.unlink(filename)