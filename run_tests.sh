#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/edeposit/amqp/pdfgen"

py.test "src/edeposit/amqp/pdfgen/tests" -vv