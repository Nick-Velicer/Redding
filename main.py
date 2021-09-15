# Nick Velicer, 8/23
# a control file to dictate Redding's startup and runtime behavior
import sys
import subprocess
import os
import mainActions
import time
from datetime import date


#a slightly slower print just because it feels more solid
def sPrint(string):
    print(string)
    time.sleep(.08)


def startup(filepath):
    startDict = mainActions.readAttributes(filepath)
    startChoice = "0"
    #reading from JSON for Prepared Initial Startup Scripts, or P.I.S.S. for short
    sPrint("\nSelect from below:")
    inSetup = False
    while not inSetup:
        for i in startDict:
            sPrint(list(i.keys())[0])
        sPrint("None")
        startChoice = str(input("Startup choice: "))
        if startChoice == "None":
            break
        loggedI = -1
        for i in startDict:
            if list(i.keys())[0] == startChoice:
                inSetup = True
                loggedI = i
                break
        print(list(loggedI.values())[0])
        if inSetup:
            os.system(list(loggedI.values())[0])
        else:
            sPrint("That is not a startup option, try again.\n")

def menu():
    menuChoice = "0"
    exitChoice = 5
    today = date.today()
    while int(menuChoice) != exitChoice:
        sPrint("What would you like to do?")
        sPrint("1: Make adjustments")
        sPrint("2: Edit scripts")
        sPrint("3: Run a script")
        sPrint("4: Add log")
        sPrint("5: Exit")
        menuChoice = input("Choice: ")
        if menuChoice == "1":
            mainActions.maintain(pathtoRestart, pathtoProject)
        elif menuChoice == "2":
            mainActions.addAttribute("startup", "New startup option", "Path to script", False)
            # add option for adjusting by subtracting/editing
        elif menuChoice == "3":
            startup(pathtoStartup)
        elif menuChoice == "4":
            mainActions.addAttribute("logs", today.strftime("%m/%d/%y"), "Log message", True)
    exit()


if __name__ == '__main__':
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    time.sleep(1)
    # r at the front is to prevent \n shenanigans
    pathtoBatch = r"C:\Redding\scripts\StartRedding.bat"
    pathtoProject = r"C:\Redding\src\main.py"
    pathtoStartup = r"C:\Redding\data\startup.json"
    pathtoRestart = r"C:\Redding\scripts\RestartRedding.bat"
    sPrint("\n")
    sPrint("  .oooooooooooooo+++ossssss-.`")
    sPrint("   -osssssss +::: // +osssssso+-")
    sPrint("    -sssssss-         `. - +ssssss-")
    sPrint("    .sssssss.              /sssss-")
    sPrint("     .ssssss:              `ssso:")
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
    sPrint("`::::::::-                    '`. -::-`")

    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            sPrint("Looked for startup file at " + pathtoStartup)
            if not os.path.isfile(pathtoStartup):
                sPrint("No startup options found")
            else:
                startup(pathtoStartup)
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
