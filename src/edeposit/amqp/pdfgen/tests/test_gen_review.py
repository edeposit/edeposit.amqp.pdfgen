#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os
import json
import specialization
from structures.requests import GenerateReview


# Variables ===================================================================



# Functions & classes =========================================================
def test_review():
    example_fn = os.path.join(
        os.path.dirname(__file__),
        "example_metadata.json"
    )

    with open(example_fn) as f:
        example_data = f.read()
        example_dict = json.loads(example_data)

    req = GenerateReview(
        **example_dict
    )

    with open("review_test.pdf", "wt") as f:
        result = specialization.get_review(req)
        result.seek(0)

        f.write(
            result.read()
        )