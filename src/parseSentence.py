#Nick Velicer, 10/10
#parses a sentence and returns a request to the data to construct a sentence

import nltk
import time


#a slightly slower print just because it feels more solid
#copied from main.py
def sPrint(string):
    print(string)
    time.sleep(.08)


def interpretRequest(string):
    tokens = nltk.word_tokenize(string)
    tokens = nltk.pos_tag(tokens)
    possibleSubjects = []
    possibleActions = []
    for i in range(len(tokens)):
        if tokens[i][1] == "NN" or tokens[i][1] == "NNP":
            possibleSubjects.append(tokens[i][0])
        if tokens[i][1] == "VB" or tokens[i][1] == "VB":
            possibleActions.append(tokens[i][0])
    
    sPrint("Interpreted subjects: ")
    for i in range(len(possibleSubjects)):
        sPrint(possibleSubjects[i] + "\n")
    sPrint("Interpreted actions: ")
    for i in range(len(possibleActions)):
        sPrint(possibleActions[i] + "\n")


def getSubjects(string):
    tokens = nltk.word_tokenize(string)
    tokens = nltk.pos_tag(tokens)
    possibleSubjects = []
    for i in range(len(tokens)):
        if tokens[i][1] == "NN" or tokens[i][1] == "NNP":
            possibleSubjects.append(tokens[i][0])
    return possibleSubjects


def getActions(string):
    tokens = nltk.word_tokenize(string)
    tokens = nltk.pos_tag(tokens)
    possibleActions = []
    for i in range(len(tokens)):
        if tokens[i][1] == "VB" or tokens[i][1] == "VB":
            possibleActions.append(tokens[i][0])
    return possibleActions
