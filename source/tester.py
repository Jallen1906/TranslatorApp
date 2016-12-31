#!/usr/bin/python
# -*- coding: latin-1 -*-
import translator

if __name__ == "__main__":
    print "Starting test..."
    googleTrans = translator.GoogleApiTranslator("fr")
    print googleTrans.language
    print googleTrans.translateWord("Bonjour")
    print googleTrans.translateSentence("Bonjour obscurité, mon vieux ami")
    print googleTrans.translateParagraph("Bonjour obscurité, mon vieux ami. Je suis venu parler avec vous encore.")
    print googleTrans.translate("Bonjour obscurité, mon vieux ami. Je suis venu parler avec vous encore.")
    misword = "bojour"
    misspelltest = googleTrans.translate(misword)
    if misspelltest.lower() == misword or misspelltest == "":
        print "Mispelt test passed"
    else:
        print misspelltest + " was returned. Mispelt test failed"
