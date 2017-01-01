#!/usr/bin/python
#
# Main translator class for the FrenchApp - this should be faily abstract and instead be derived from with more specific implementation based on whatever API
#


import sys
import re
from abc import *
import urllib2
import urllib
import HTMLParser
import utils

class Translator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialise(self, language):
        # Standard call for whatever the derived class must do in order to intialise itself or any connections is must make to the API - should be all contained within this function.
        # returns whether the initialisation was successful - this can be used for error handling etc
        return False
    @abstractmethod
    def translate(self, inputText):
        # Automatically detects which tranlate function to call
        returnString = ""
        if len(inputText) <= 0:
            print "Incorrect format of input text."
        # With no spaces, assume inputText is a single word.
        elif inputText.find(" ") == -1:
            returnString = self.translateWord(inputText)
        # With no full-stops, assume inputText is a single sentence.
        elif inputText.find(".") == -1:
            returnString = self.translateSentence(inputText)
        # Otherwise, assume inputText is a paragraph.
        else:
            returnString = self.translateParagraph(inputText)
        #TODO: implement a check for \n and call it translatePage.
        return returnString

    @abstractmethod
    def translateWord(self, inputText):
        """Translates an individual word"""
    @abstractmethod
    def translateSentence(self, inputText):
        """Translates an individual sentence. May end up calling """
    @abstractmethod
    def translateParagraph(self, inputText):
        """Translates an entire paragraph"""
    #languages = ["fr", "en", "ge"]

# Implementation of the Google API derivation of the Translator ABC
#TODO: Add different encoding if language chosen is different.
class GoogleApiTranslator(Translator):
    
    base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    regexp = r'class="t0">(.*?)<'
    agent = {'User-Agent':
            "Mozilla/4.0 (\
                    compatible;\
                    MSIE 6.0;\
                    Windows NT 5.1;\
                    SV1;\
                    .NET CLR 1.1.4322;\
                    .NET CLR 2.0.50727;\
                    .NET CLR 3.0.04506.30\
                    )"}
    def unescape(self, text):
        if (sys.version_info[0] < 3):
            parser = HTMLParser.HTMLParser()
        else:
            parser = html.parser.HTMLParser()
        return (parser.unescape(text))
    def __init__(self, language):
        self.initialise(language)
    def initialise(self, language):
        returnCode = False
        if language in utils.Languages:
            self.language = language
            returnCode = True
            returnCode = self.checkConnection()
        else :
            print "{} is not a valid language.".format(language)
            returnCode = False
        return returnCode
    def translateWord(self, inputText):
        return self.googleTranslate(inputText)
    def translateSentence(self, inputText):
        return self.googleTranslate(inputText)
        #return inputText, self.language
    def translateParagraph(self, inputText):
        return self.googleTranslate(inputText)

        #return inputText, self.language
    def translate(self,  inputText):
        return super(GoogleApiTranslator, self).translate(inputText)
    def googleTranslate(self, inputText):
        inputText = urllib.quote_plus(inputText)
        link = self.base_link % ('en', self.language, inputText)
        request = urllib2.Request(link, headers=self.agent)
        raw_data = urllib2.urlopen(request).read()
        return self.parseXml(raw_data)

    def checkConnection(self):
        '''Send some data to the Google API website to see if there's a connection available'''
        return True
    def parseXml(self, rawData):
        re_result = re.findall(self.regexp, rawData)
        if len(re_result) == 0:
            print "Couldn't match regex - {}\n".rawData
            return ""
        else:
            return self.unescape(re_result[0])
Translator.register(GoogleApiTranslator)
