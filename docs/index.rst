edeposit.amqp.pdfgen
====================

This module is used to dynamically generate some of the PDF documents, which are required by the E-deposit project website.

API
---

.. toctree::
    :maxdepth: 1

    /api/pdfgen
    /api/pdfgen.specialization
    /api/pdfgen.translator

AMQP communication
------------------

.. toctree::
    :maxdepth: 1

    /api/pdfgen.structures.requests
    /api/pdfgen.structures.responses


Installation
------------
Installation at debian systems is really easy::

    pip install edeposit.amqp.pdfgen


(Open)Suse
++++++++++

OpenSuse by default doesn't have installed the FreeSerif_ fonts, which are
required for this package.

.. _FreeSerif: http://savannah.gnu.org/projects/freefont/

You can install it using following commands::

    cd /tmp
    wget http://213.174.32.130/sles/distribution/11.0-SP1/repo/sdk/suse/noarch/freefont-0.20080323-1.17.noarch.rpm
    zypper install freefont-0.20080323-1.17.noarch.rpm


Source code
-----------
This project is released as opensource (GPL) and source codes can be found at
GitHub:

- https://github.com/edeposit/edeposit.amqp.pdfgen


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`