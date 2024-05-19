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
import nltk

#globals
reddingHome = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
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
            ask = input("Add a log (y/n)?: ")
            if ask == "y":
                today = date.today()
                mainActions.addAttribute("logs", today.strftime("%m/%d/%y"), "Log message", True, True)
                
    tempStartupList = []
    for i in os.listdir(filepath):
        tempStartupList.append(i)

    if len(tempStartupList) == 0:
        return

    os.system("cls")
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
    menuChoice = "0"
    global handler
    #if it's a one liner, add a call in here
    #otherwise add it as a function in mainActions.py

    #format: printed text, function to call, list of arguments
    #python freaks out when you have the actual calls declared, so the arguments are in separately
    menuChoices = [["Run A Script", startup, [pathtoStartup, False]],
                   ["Internet Search", mainActions.lookUp, []],
                   ["System Files", os.system, ["explorer"]],
                   ["Edit Scripts", mainActions.editScripts, [reddingHome + "\\scripts\\main"]],
                   ["Settings", os.system, ["notepad " + reddingHome + "\\data\\config.json"]]]
    
    devOptions = [["Make Adjustments", mainActions.maintain, [pathtoRestart, pathtoProject]],
                  ["Ask A Question", mainActions.request, []],
                  ["View Knowledge Network", mainActions.viewNetwork, [reddingHome + "\\data\\parsenetwork.json", handler]],
                  ["Notes", os.system, ["notepad " + reddingHome + "\\data\\notes.txt"]]]

    menuArr = []
    
    while int(menuChoice) != len(menuArr)+1:
        os.system("cls")
        if mainActions.readConfig("Developer Mode"):
            menuArr = menuChoices + devOptions
        else:
            menuArr = menuChoices
        print("")
        sPrint("What would you like to do?")
        for i in range(len(menuArr)):
            sPrint(str(i+1) + ": " + menuArr[i][0])
        sPrint(str(len(menuArr)+1) + ": Exit")
        menuChoice = input("Choice: ")
        if int(menuChoice) < 0 or (not menuChoice.isdigit()):
            sPrint("Error: Input Out Of Range")
        elif int(menuChoice) == len(menuArr)+1:
            #let things fall through and program exit
            break
        else:
            menuArr[int(menuChoice)-1][1](*menuArr[int(menuChoice)-1][2])


if __name__ == '__main__':

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)
    pathtoBatch = reddingHome + "\\scripts\\StartRedding.bat"
    pathtoProject = reddingHome
    pathtoStartup = reddingHome + "\\scripts\\main"
    pathtoRestart = reddingHome + "\\scripts\\RestartRedding.bat"
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
        handler.initializeNetwork(reddingHome + "\\data\\parsenetwork.json")
        if (reddingHome + "\\.venv\\Lib\\nltk_data") not in nltk.data.path:
            nltk.data.path.append(reddingHome + "\\.venv\\Lib\\nltk_data")
        
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

        handler.backupNetwork(reddingHome + "\\data\\parsenetwork.json")
        exit()
    else:
        sPrint("no argument specified")
