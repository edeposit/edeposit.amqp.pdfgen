#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Ubuntu packages: clamav clamav-daemon
# Suse packages: clamav

import os
import os.path
import shutil

from setuptools import setup, find_packages
from distutils.command.sdist import sdist

try:
    from docs import getVersion
except ImportError:  # during packaging, docs are moved to html_docs
    from html_docs import getVersion


changelog = open('CHANGES.rst').read()
long_description = "\n\n".join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    changelog
])


class BuildSphinx(sdist):
    """
    Generates sphinx documentation, puts it into html_docs/, packs it to
    package and removes unused directory.
    """
    def run(self):
        d = os.path.abspath('.')
        DOCS = d + "/" + "docs"
        DOCS_IN = DOCS + "/_build/html"
        DOCS_OUT = d + "/html_docs"

        if not self.dry_run:
            print "Generating the documentation .."

            os.chdir(DOCS)
            os.system("make clean")
            os.system("make html")

            if os.path.exists(DOCS_OUT):
                shutil.rmtree(DOCS_OUT)

            shutil.copytree(DOCS_IN, DOCS_OUT)
            shutil.copy(DOCS + "/__init__.py", DOCS_OUT)  # for getVersion()
            os.chdir(d)

        sdist.run(self)

        if os.path.exists(DOCS_OUT):
            shutil.rmtree(DOCS_OUT)


setup(
    name='edeposit.amqp.pdfgen',
    version=getVersion(changelog),
    description="E-Deposit's AMQP bindings to PDF generation libraries.",
    long_description=long_description,
    url='https://github.com/edeposit/edeposit.amqp.pdfgen/',

    author='Edeposit team',
    author_email='edeposit@email.cz',

    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    license='GPL2+',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    # package_data={'': ['edeposit/amqp/ltp/xslt/*.xsl']},

    # scripts=[''],

    namespace_packages=['edeposit', 'edeposit.amqp'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        "rst2pdf",
    ],
    extras_require={
        "test": [
            "pytest",
            "pdfminer"
        ],
        "docs": [
            "sphinx",
            "sphinxcontrib-napoleon",
        ]
    },

    cmdclass={'sdist': BuildSphinx}
)
