#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from structures import *
from translator import gen_pdf
from specialization import get_contract


# Functions & classes =========================================================
def _instanceof(instance, class_):
    """Check type by matching ``.__name__``."""
    return type(instance).__name__ == class_.__name__


def reactToAMQPMessage(message, UUID=None):
    """
    React to given (AMQP) message. `message` is usually expected to be
    :py:func:`collections.namedtuple` structure filled with all necessary data.

    Args:
        message (\*Request class): only :class:`.ConversionRequest` class is
                                   supported right now

        UUID (str):                unique ID of received message

    Returns:
        ConversionResponse: response filled with data about conversion and\
                            converted file.

    Raises:
        ValueError: if bad type of `message` structure is given.
    """
    if _instanceof(message, GenerateContract):
        return get_contract(
            message.firma,
            message.pravni_forma,
            message.sidlo,
            message.ic,
            message.dic,
            message.zastoupen,
            message.jednajici,
        ).read()
    elif _instanceof(message, RST2PDF):
        return gen_pdf(
            rst_content=message.rst_content,
            style_text=message.style,
            header=message.header,
            footer=message.footer
        )

    raise ValueError(
        "Unknown type of request: '" + str(type(message)) + "'!"
    )
