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


def run_batfile(path):
    subprocess.call([path])


def maintain(restartPath, projectPath):
    subprocess.call("pycharm64.exe " + projectPath)
    print("I will need to reinitialize for your changes to go through.")
    restartOption = input("Would you like to do so now? (y/n)")
    if restartOption == "y":
        os.system(restartPath)
        exit()
    else:
        print("No problem, those will be in on next startup")


#key: log/script..., keyPhrase: "new thing identifier?: ", valuePhrase: "new thing?", keyProvided: true/false
def addAttribute(key, keyPhrase, valuePhrase, keyProvided):
    file = "C:\Redding\data\\" + key + ".json"
    if not os.path.isfile(file):
        print("No " + key + " file found, creating new file")
        with open(file, 'w') as outfile:
            initOut = str({"\"%s\"" % key: []}).replace("'", "")
            outfile.write(initOut)
            outfile.close()

    if os.path.isfile(file):
        aFile = ar.AttributeReader(file)
        createNew = "y"
        while createNew == "y":
            #checking if the user needs to provide a key/title or if it should automatically be keyed (i.e. date)
            if keyProvided:
                newKey = keyPhrase
            else:
                newKey = input(str(keyPhrase + ": "))
            newValue = input(str(valuePhrase + ": "))
            aFile.add(newKey, newValue)
            createNew = input("\nAdd another " + key + "? (y/n): ")
    else:
        print("There was a problem opening the " + key + " file.")


def readAttributes(file):
    aFile = ar.AttributeReader(file)
    return aFile.read()[os.path.splitext(ntpath.basename(file))[0]]
