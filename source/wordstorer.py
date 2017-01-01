#!/usr/bin/python
# Word storage classes. WordStorer is the ABC, with derivatives of both offline (XML, CSV etc) and online (using a database, for instance) available.
#TODO: Decide appropriate storage class - dictionary or a more advanced dictionary.
from abc import *
import utils
class WordStorer:
    __metaclass__ = ABCMeta
    def __init__(self):
     ''' '''    


# This class will store words in volatile memory i.e. RAM whilst the program is running, and then on either quit or 'save' the words can then be stored to NV memory i.e. HDD.
class OfflineWordStorer:
    def __init__ (self, lang):
        if lang in utils.Languages:
            self.Language = lang
        else:
            raise ValueError('Invalid language inputted in OfflineWordStorer ctor - see utils.Languages for allowed values.')

    def loadWordsToMemory(self):
        ''' This method will open the file with the dictionary stored on the PC and read the contents to RAM for this session'''

    def saveSession(self):
        ''' Writes the current session's dictionary to file. '''

    def addEntry(self, lang1, lang2):
        if type(lang1) is not str or type(lang2) is not str:
            raise TypeError('Invalid type in OfflineWordStorer.addEntry - check entry types to ensure they are strings.')
        self.Dictionary[lang1] = lang2
    def removeEntry(self, lang1):
        if type(lang1) is not str:            
            raise TypeError('Invalid type in OfflineWordStorer.removeEntry - check entry type to ensure it is a string.')
        del self.Dictionary[lang1]
    def printEntries(self):
        print "{}".format(self.Language)
        for lang1, lang2 in self.Dictionary:
            print "{:s} : {:s}".format(lang1, lang2)
    def getEntries(self):
        return self.Dictionary
    def getRandomEntry(self):
        return self.Dictionary.iteritems()[0]
    Language = ""
    Dictionary = {}


WordStorer.register(OfflineWordStorer)
