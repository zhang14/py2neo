#!/usr/bin/env python

from distutils.core import setup

setup(
	name="py2neo",
	version="1.2.0",
	description="Python bindings to Neo4j",
	long_description="""The py2neo project provides bindings between Python and Neo4j via its RESTful web service interface. It attempts to be both Pythonic and consistent with the core Neo4j API and is compatible with Python 3.""",
	author="Nigel Small",
	author_email="py2neo@nigelsmall.net",
	url="http://py2neo.org/",
	package_dir={"": "src"},
	packages=["py2neo"],
	license="Apache License, Version 2.0",
	classifiers=[]
)