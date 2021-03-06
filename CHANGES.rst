Changelog
=========

0.5.1
-----
    - Fixed e-depozit -> e-deposit.

0.5.0
-----
    - Contract text updated.

0.4.11
------
    - Improved resoliton of the logo. Fixed #32.
    - Added annotation to review. Fixed #31.

0.4.10
------
    - Contract text updated as requested.

0.4.0 - 0.4.9
-------------
    - Update of the descriptors in the requests generator.
    - Removed unused things from setup.py.
    - Added special style for review. There is now more space for data.
    - Tests metadata updated.
    - Added escaping of the sphinx syntax in data fields.
    - run_tests.sh: Changed PYTHONPATH variable to prioritize local path.
    - Updated text of the contract.
    - Small bugfix of contract text.
    - Another small bugfix.
    - Added new parts into cotract.
    - Fixed issue #23 - problem with very long links.
    - TrueType fonts should be now included in pdf.
    - Added argument passing to ``run_tests.sh``.
    - Removed colon from the end of the Producer's name.
    - Blank strings are now recognized as "Nezvoleno".
    - Name of the director of Czech National Library removed from contract text.

0.3.0 - 0.3.5
-------------
    - Added support for QR code.
    - Added logo into contract template.
    - Small improvements of templates.
    - ``reactToAMQPMessage()`` parameters modified.
    - Documentation of ``reactToAMQPMessage()`` updated.
    - Formating of the contract updated.
    - Added installation notes specific to Suse systems.
    - Fixed bugs specific to OpenSuse.
    - Tests moved to the root of the package.
    - "jednajici" removed from contract.
    - Formating of the contract updated - for the last time I hope.

0.2.0 - 0.2.4
-------------
    - Added logo to review.
    - requests_template.py renamed to requests_template.txt.
    - Fixed #16 - bug in setuptools. HTML generation command had to be removed.
    - Fixed small bug in contract generator.
    - Added internal_url field.
    - review_example.pdf is now saved to test directory. This is useful for showing the review to other people.
    - Removed default arguments in GenerateReview structure.
    - Added experimental utf-8 skip.

0.1.0
-----
    - Project created.