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
import time
import json
import baseProcedureHandler as bph
import multiRelationalNetwork as mrn

reddingHome = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

def sPrint(string):
    print(string)
    time.sleep(.08)

def run_batfile(path):
    p = subprocess.Popen([path])
    p.wait()

def readConfig(setting):
    file = open(reddingHome + "\\data\\config.json")
    configuration = json.load(file)
    file.close()
    return configuration[setting]


def setConfig(setting, newState):
    file = open(reddingHome + "\\data\\config.json")
    configuration = json.load(file)
    file.close()
    configuration[setting] = newState
    with open(reddingHome + "\\data\\config.json", "w") as outfile:
        json.dump(configuration, outfile)
    return configuration[setting]

def maintain(restartPath, projectPath):
    os.system(readConfig("Editor") + " " + projectPath)
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


def editScripts(parentPath):
    tempStartupList = []
    for i in os.listdir(parentPath):
        tempStartupList.append(i)

    if len(tempStartupList) == 0:
        return
    sPrint("\nChoose a script to edit " + parentPath + ":")
    for i in range(len(tempStartupList)):
        sPrint(str(i + 1) + ": " + tempStartupList[i][:-4])
    choice = input("Choice: ")
    while not (int(choice) - 1 <= len(tempStartupList) and int(choice) - 1 >= 0):
        sPrint("Error: Please input within the given range")
        choice = input("Choice: ")
    os.system("notepad " + parentPath + "\\" + tempStartupList[int(choice)-1])





