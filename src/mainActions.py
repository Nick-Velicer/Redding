#Nick Velicer, 8/25
#primary functions of Redding

#script list/separate menu for executing scripts, eventually no list
#options to open self up
import os
import subprocess
from multiprocessing import Process, freeze_support
import json
import attributeReader as ar
import ntpath
import parseSentence
import baseProcedureHandler as bph
import multiRelationalNetwork as mrn

reddingHome = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

def run_batfile(path):
    subprocess.call([path])


def maintain(restartPath, projectPath):
    subprocess.call("pycharm64.exe " + projectPath)
    print("\nI will need to reinitialize for your changes to go through.")
    restartOption = input("Would you like to do so now (y/n)?: ")
    if restartOption == "y":
        os.system(restartPath)
        exit()
    else:
        print("No problem, those will be in on next startup")


#key: log/script..., keyPhrase: "new thing identifier?: ", valuePhrase: "new thing?", keyProvided: true/false, repeats: true/false
def addAttribute(key, keyPhrase, valuePhrase, keyProvided, repeats):
    file = reddingHome + "\\data\\" + key + ".json"
    if not os.path.isfile(file):
        print("No " + key + " file found, creating new file")
        with open(file, 'w') as outfile:
            initOut = str({"\"%s\"" % key: []}).replace("'", "")
            outfile.write(initOut)
            outfile.close()

    if os.path.isfile(file):
        aFile = ar.AttributeReader(file)
        createNew = "y"
        allowItr = True
        while createNew == "y" and allowItr:
            #checking if the user needs to provide a key/title or if it should automatically be keyed (i.e. logs)
            if keyProvided:
                newKey = keyPhrase
            else:
                newKey = input(str(keyPhrase + ": "))
            newValue = input(str(valuePhrase + ": "))
            aFile.add(newKey, newValue)
            allowItr = repeats
            if allowItr:
                if key[-1] == "s":
                    tempKey = key[:-1]
                    createNew = input("\nAdd another " + tempKey + "? (y/n): ")
                else:
                    createNew = input("\nAdd another " + key + "? (y/n): ")
    else:
        print("There was a problem opening the " + key + " file.")


def readAttributes(file):
    aFile = ar.AttributeReader(file)
    return aFile.read()[os.path.splitext(ntpath.basename(file))[0]]


def removeAttributes(file, key):
    testDict = readAttributes(file)
    flag = False
    for i in testDict:
        if list(i.keys())[0] == key:
            flag = True
            break
    if not flag:
        return
    aFile = ar.AttributeReader(file)
    aFile.remove(key)


def request():
    testAgain = True
    while (testAgain):
        parseSentence.interpretRequest(input("Test phrase: "))
        another = input("Try another phrase? (y/n): ")
        if another == "y":
            testAgain = True
        else:
            testAgain = False


def viewNetwork(path, handlerRef):
    handlerRef.printNetwork()
    addCheck = input("Add a word (y/n)?: ")
    if addCheck == "y":
        while addCheck == "y":
            newWord = input("What word would you like to add?: ")
            handlerRef.addWord(newWord)
            addCheck = input("Add another word (y/n)?: ")

