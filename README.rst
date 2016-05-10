========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/vimeopy/badge/?style=flat
    :target: https://readthedocs.org/projects/vimeopy
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/thundersystems/vimeopy.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/thundersystems/vimeopy

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/thundersystems/vimeopy?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/thundersystems/vimeopy

.. |requires| image:: https://requires.io/github/thundersystems/vimeopy/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/thundersystems/vimeopy/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/thundersystems/vimeopy/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/thundersystems/vimeopy

.. |version| image:: https://img.shields.io/pypi/v/vimeo.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/vimeo

.. |downloads| image:: https://img.shields.io/pypi/dm/vimeo.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/vimeo

.. |wheel| image:: https://img.shields.io/pypi/wheel/vimeo.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/vimeo

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/vimeo.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/vimeo

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/vimeo.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/vimeo


.. end-badges

Package for python based on Vimeo API

* Free software: BSD license

Installation
============

::

    pip install vimeo

Documentation
=============

https://vimeopy.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
