# !/usr/bin/python2.7 -S
# coding:utf-8
# -*- coding: utf-8 -*-

##########################################
##-----------Anurag Banerjee------------##
##---------------CS 7030----------------##
##-----------  Assignment 1  -----------##
##########################################


import io
import re

# Global variables
readText = ""
sentences = []
result = []


def getFile(fname):
    '''
    This function opens the file in @fname and returns a read stream
    :param fname:
    :return: the text stream
    '''

    with io.open(fname, encoding="utf-8") as f:
        try:
            return f.read()
        finally:
            f.close()


def readDoc():
    '''
    This function will read in the text file containing Indic lang. script and store it in the 'doc' variable.
    Holds the entire text document. Not a good idea when document is large. For larger documents, modify to read sentences
    from the file, one at a time.
    :return:
    '''

    global readText
    readText = getFile("E:\\AnuragData\\Documents\\Projects\\PythonProjects\\IR_courseProj\\CS_7030\\sample-hindi.txt")
    doc = unicode(readText).encode('utf8')
    print ("-----Displaying the file just read-----")
    print doc
    print ("-------------end of file---------------")


def writeToFile(stringList):
    '''
    This function is used to write the result back to a file on disk.
    :return:
    '''
    result = ""
    for strings in stringList:
        result += strings
    try:
        writer = open("E:\\AnuragData\\Documents\\Projects\\PythonProjects\\IR_courseProj\\CS_7030\\sample-hindi-output.txt",
                      'w+')
        # w+ means overwrite - use with care
        writer.write(result.encode("UTF-8"))
    finally:
        writer.close()


def readSentence():
    '''
    From a text made up of multiple sentences, extract each sentence and store in a list. In
    Hindi the sentence delimiter is the "Poorna Veeram"
    :return:
    '''
    global readText, sentences
    sentences = readText.split(u"।")
    for i, s in enumerate(sentences):  # trying to remove leading and trailing spaces
        sentences[i] = re.sub(ur'[-,;\']*', '', s.strip(' \t\n\r\"'))
    showSentences(sentences)


def showSentences(sentList):
    '''
    Given a list of sentences, display the sentences on screen in Unicode encoding
    :param sentList:
    :return:
    '''
    print ("\n\n--------Showing set of sentences-------")
    for sentence in sentList:
        print (unicode(sentence).encode("UTF-8"))
    print ("--------------------------------------")


def extractWords(string):
    '''
    Given a sentence via the parameter @string, return a list of words contained in the sentence
    :return:
    '''
    words = string.split(u" ")
    return words


def porterLikeStemmer(word):  # implemented for Hindi
    '''
    When its called Porter like, the only similarity is that it is also a suffix stripping algorithm; otherwise,
    it is not based on the Porter algorithm for english language.
    :param word:
    :return:
    '''
    suffixes = {
        s1: [u"ा", u"ो", u"ौ", u"े", u"ै", u"ू", u"ु", u"ी", u"ि"],
        s2: [u"कर", u"ाओ", u"िए", u"ाई", u"ाए", u"ने", u"नी", u"ना", u"ते", u"ीं", u"ती", u"ता", u"ाँ", u"ां", u"ों", u"ें"],
        s3: [u"ाकर", u"ाइए", u"ाईं", u"ाया", u"ेगी", u"ेगा", u"ोगी", u"ोगे", u"ाने", u"ाना", u"ाते", u"ाती", u"ाता", u"तीं", u"ाओं", u"ाएं", u"ुओं", u"ुएं", u"ुआं"],
        s4: [u"ाएगी", u"ाएगा", u"ाओगी", u"ाओगे", u"एंगी", u"ेंगी", u"एंगे", u"ेंगे", u"ूंगी", u"ूंगा", u"ातीं", u"नाओं", u"नाएं", u"ताओं", u"ताएं", u"ियाँ", u"ियों", u"ियां"],
        s5: [u"ाएंगी", u"ाएंगे", u"ाऊंगी", u"ाऊंगा", u"ाइयाँ", u"ाइयों", u"ाइयां"]
    }

    for affix in s5, s4, s3, s2, s1:
        if len(word) > affix + 1:
            for suf in suffixes[affix]:
                if word.endswith(suf):
                    return word[:-affix]
    return word


def lovinsLikeStemmer(word):  # implemented for Hindi
    '''
    Has to be a table lookup approach, otherwise not related to Lovins
    :param word:
    :return:
    '''
    #


def doStemming():
    '''
    This function performs the stemming action
    :return:
    '''
    global sentences, result
    readDoc()
    readSentence()
    for sentence in sentences:
        words = extractWords(sentence)
        newSentence = ""
        for word in words:
            newWord = porterLikeStemmer(word)
            newSentence += (newWord + " ")
        result.append(newSentence.strip(" "))

    showSentences(result)


if __name__ == "__main__":
    doStemming()
    writeToFile(result)

