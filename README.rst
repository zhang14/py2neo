Py2neo v4
=========
.. image:: https://img.shields.io/github/license/technige/py2neo.svg
   :target: https://www.apache.org/licenses/LICENSE-2.0
   :alt: License

**Py2neo** is a client library and toolkit for working with `Neo4j <https://neo4j.com/>`_ from within `Python <https://www.python.org/>`_ applications and from the command line.
The library wraps the `official driver <https://github.com/neo4j/neo4j-python-driver>`_, adding support for HTTP, a higher level API, an OGM, admin tools, an interactive console, a Cypher lexer for Pygments and many other bells and whistles.
Unlike previous releases, Py2neo v4 no longer requires HTTP and can work entirely through Bolt.


Installation
------------
.. image:: https://img.shields.io/pypi/v/py2neo.svg
   :target: https://pypi.python.org/pypi/py2neo
   :alt: PyPI version

.. image:: https://img.shields.io/travis/technige/py2neo/v4.svg
   :target: https://travis-ci.org/technige/py2neo
   :alt: Build Status

.. image:: https://img.shields.io/coveralls/github/technige/py2neo/v4.svg
   :target: https://coveralls.io/github/technige/py2neo?branch=v4
   :alt: Coverage Status

To install the latest stable version of py2neo, simply use pip:

.. code-block::

    $ pip install py2neo

Or to install the latest bleeding edge code directly from GitHub, use:

.. code-block::

    $ pip install git+https://github.com/technige/py2neo.git#egg=py2neo


Note that code installed directly from GitHub is likely to be unstable.
Your mileage may vary.


Requirements
------------

.. image:: https://img.shields.io/pypi/pyversions/py2neo.svg
   :target: https://www.python.org/
   :alt: Python versions

.. image:: https://img.shields.io/badge/neo4j-3.0%2C%203.1%2C%203.2%2C%203.3%2C%203.4-blue.svg
   :target: https://neo4j.com/
   :alt: Neo4j versions

The following versions of Python and Neo4j are supported:

- Python 2.7 / 3.4 / 3.5 / 3.6 / 3.7-dev / PyPy
- Neo4j 3.0 / 3.1 / 3.2 / 3.3 / 3.4 (the latest point release of each version is recommended)

Note also that Py2neo is developed and tested under **Linux** using standard CPython distributions.
While other operating systems and Python distributions may work, support for these is not available.


Contact
-------

For more information, read the `handbook <http://py2neo.org/v4>`_.

To get in touch, contact me via `email <mailto:py2neo@nige.tech>`_ or on `Twitter <https://twitter.com/technige>`_.
