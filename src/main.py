# Nick Velicer, 8/23
# a control file to dictate Redding's startup and runtime behavior
import sys
import subprocess
import os
import mainActions
import time
import datetime
from datetime import date
import baseProcedureHandler as bph

handler = bph.BaseProcedureHandler()
#a slightly slower print just because it feels more solid
def sPrint(string):
    print(string)
    time.sleep(.08)

def startup(filepath, firstCall):
    if firstCall:
        ask = input("Do you have a moment (y/n)?: ")
        if ask == "y":
            mainActions.addAttribute("wellness", datetime.datetime.now().strftime("%m/%d/%Y %H:%m"), "How are you feeling on a scale from 1-10?", True, False)
    tempStartupList = []
    for i in os.listdir(filepath):
        tempStartupList.append(i)

    if len(tempStartupList) == 0:
        return

    sPrint("\nCurrent scripts in " + filepath + ":")
    for i in range(len(tempStartupList)):
        sPrint(str(i + 1) + ": " + tempStartupList[i][:-4])
    sPrint(str(len(tempStartupList)+1) + ": None")
    choice = input("Choice: ")
    while not (int(choice)-1 <= len(tempStartupList) and int(choice)-1 >= 0):
        sPrint("Error: Please input within the given range")
        choice = input("Choice: ")
    if (int(choice) == len(tempStartupList)+1):
        return
    print()
    os.system(str(filepath) + "\\" + str(tempStartupList[int(choice)-1]))

def menu():
    #make this array-based
    menuChoice = "0"
    today = date.today()
    menuChoices = ["Make adjustments",
                   "Run a script",
                   "Add log",
                   "Ask a question",
                   "View Knowledge Network"]
    while int(menuChoice) != len(menuChoices)+1:
        print("")
        sPrint("What would you like to do?")
        for i in range(len(menuChoices)):
            sPrint(str(i+1) + ": " + menuChoices[i])
        sPrint(str(len(menuChoices)+1) + ": Exit")
        menuChoice = input("Choice: ")
        if menuChoice == "1":
            mainActions.maintain(pathtoRestart, pathtoProject)
        elif menuChoice == "2":
            startup(pathtoStartup, False)
        elif menuChoice == "3":
            mainActions.addAttribute("logs", today.strftime("%m/%d/%y"), "Log message", True, True)
        elif menuChoice == "4":
            mainActions.request()
        elif menuChoice == "5":
            global handler
            mainActions.viewNetwork("C:\\Redding\\data\\parsenetwork.json", handler)

    handler.backupNetwork("C:\\Redding\\data\\parsenetwork.json")
    exit()


if __name__ == '__main__':
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)
    # r at the front is to prevent \n shenanigans
    pathtoBatch = r"C:\Redding\scripts\StartRedding.bat"
    pathtoProject = r"C:\Redding\src\main.py"
    pathtoStartup = r"C:\Redding\scripts\main"
    pathtoRestart = r"C:\Redding\scripts\RestartRedding.bat"
    sPrint("\n")
    sPrint("  .oooooooooooooo+++ossssss-.`")
    sPrint("   -osssssss +::: // +osssssso+")
    sPrint("    .sssssss.              /ssss")
    sPrint("     /ssssss'              .oo:   .")
    sPrint("    .oooooo/               '   .+.")
    sPrint("    .oooooo/                /-+o::")
    sPrint("    .ooooooo/.`````.. -: +oo +.")
    sPrint("   .ooooooooooooooooooo + / -")
    sPrint("   .oooooooo++oooooo+:.")
    sPrint("   /+++++++:  `-+++++++.")
    sPrint("   .+++++++:   `-/+++++/.")
    sPrint("  /+++++++:      .:/++++:`")
    sPrint("  .+++++++-         `.:/++/:.")
    sPrint(" /:+++++++-             `.: // /:.`")

    if len(sys.argv) > 1:
        handler.initializeNetwork("C:\\Redding\\data\\parsenetwork.json")
        if sys.argv[1] == "-s":
            startup(pathtoStartup, True)
            menu()
            #try and read from the options and move straight into script running

            #print options, asked for rushed or not and log day of week and time, base future asks on that
            #if not rushed ask for how feeling, give verbose description, show how felt historically based on past logs

            #subprocess.call('start /wait python main.py -c', shell=True)
            #main loop of things to do

        elif sys.argv[1] == "-c":
            menu()

    else:
        sPrint("no argument specified")
