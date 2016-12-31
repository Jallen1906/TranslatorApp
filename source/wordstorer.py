#!/usr/bin/python
# Word storage classes. WordStorer is the ABC, with derivatives of both offline (XML, CSV etc) and online (using a database, for instance) available.
from abc import *
class WordStorer:
    __metaclass__ = ABCMeta

