#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/edeposit/pdfgen"

py.test "src/edeposit/pdfgen/tests"