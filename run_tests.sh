#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/edeposit/contract"

py.test "src/edeposit/contract/tests"