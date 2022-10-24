#Nick Velicer, 8/18/22
#A collection of procedures that are parsed from Redding's word network

import multiRelationalNetwork as mrn
import json

#the current parsing network (eventually store and read in from file)
#three relations for tenses, synonyms, and relatedness
#globals for selecting between relations
tenseID = 0
synonymID = 1
relatedID = 2
inversesID = 3


def edgeDictToList(dictList):
    # [{"connection": "word", "weight": 1}, ...] -> [[word, weight], ...]
    for i in range(len(dictList)):
        dictList[i] = [dictList[i].get("connection"), dictList[i].get("weight")]
    return dictList


def edgeListToDict(dictList):
    #[[word, weight], ...] -> [{"connection": "word", "weight": 1}, ...]
    for i in range(len(dictList)):
        dictList[i] = {"connection": dictList[i][0], "weight": dictList[i][1]}
    return dictList


def mergeDicts(dict1, dict2):
    res = {**dict1, **dict2}
    return res


class Word:
    def __init__(self, name):
        self.title = name

    def __repr__(self):
        return self.title

    def __eq__(self, comparison):
        return self.title == comparison.title and self.partOfSpeech == comparison.partOfSpeech

    def asDict(self):
        #return words as strings
        return {self.title: {"definition": self.definition, "partOfSpeech": self.partOfSpeech, "tenses": self.tenses, "synonyms": self.synonyms}, "related": self.related, "inverses": self.inverses}

    title = ""
    # a short string for the word's meaning
    definition = ""
    # the part of speech that the word is
    partOfSpeech = ""
    #tenses is an array of the various tenses of the word, containing links to those similarly to synonyms
    tenses = []
    #synonyms is an array of words with similar meanings
    synonyms = []
    #related is an array of string/integer pairs, for related contexts and weights for pathfinding
    related = []
    # opposite perspective words for question/answer (ie. me/you or I/you)
    inverses = []


class BaseProcedureHandler:
    network = mrn.MRN(4)

    def __init__(self):
        self.network = mrn.MRN(4)

    def printNetwork(self):
        self.network.print(-1)

    def initializeNetwork(self, filepath):
        #read in to the structure from a file
        #formatted for word structure
        with open(filepath, "r") as read_file:
            data = json.load(read_file)
        #only reading the first word at the moment
        for wordName, wordData in data.items():
            #in the network, paths are a list but for parsing they are saved as a dictionary and then read back into a list
            newWord = Word(wordName)
            newWord.definition = wordData.get("definition")
            newWord.partOfSpeech = wordData.get("partOfSpeech")
            newWord.tenses = edgeDictToList(wordData.get("tenses"))
            newWord.synonyms = edgeDictToList(wordData.get("synonyms"))
            newWord.related = edgeDictToList(wordData.get("related"))
            newWord.inverses = edgeDictToList(wordData.get("inverses"))
            self.network.addNode(newWord, [newWord.tenses, newWord.synonyms, newWord.related, newWord.inverses])

    def backupNetwork(self, filepath):
        # get edges for each node and write the updated ones to the file
        #allows for updated adjacencies between initialization and writing
        aggregatorDictionary = {}
        for i in range(self.network.size()):
            #assuming consistent order of relationships
            #indexing to cut out the redundant edge base
            tenses = edgeListToDict(self.network.getEdges(self.network[i], tenseID)[1])
            synonyms = edgeListToDict(self.network.getEdges(self.network[i], synonymID)[1])
            related = edgeListToDict(self.network.getEdges(self.network[i], relatedID)[1])
            inverses = edgeListToDict(self.network.getEdges(self.network[i], inversesID)[1])
            newDict = {self.network[i].title: {"definition": self.network[i].definition, "partOfSpeech": self.network[i].partOfSpeech, "tenses": tenses, "synonyms": synonyms, "related": related, "inverses": inverses}}
            aggregatorDictionary = mergeDicts(aggregatorDictionary, newDict)

        with open(filepath, "w") as outfile:
            json.dump(aggregatorDictionary, outfile, indent=4)
        print("Knowledge Network successfully backed up")

    def parseRequest(self, action, subject):
        #action is a function call
        #subject is a value
        #try catch for if arguments work? maybe an array of things?
        string = action

    def wordAssociation(self, start, end):
        #dijkstras algorithm, trace path between nodes and outline path
        string = start

    def addWord(self, string):
        #prompt for tense
        #recursively prompt for words it's like and add links
        #if it's a synonym of a word duplicate that word's links and add a link between the two
        if not self.network.contains(string):
            newAddition = Word(string)
            newDef = input("What is the definition of " + string + "?: ")
            newAddition.definition = newDef
            pOS = input("What is the part of speech?: ")
            newAddition.partOfSpeech = pOS
            tenses = []
            synonyms = []
            inverses = []
            related = []
            if pOS == "verb":
                past = input("Additional tense (past/present):  ")
                tenses.append(past)
            if pOS == "personal pronoun":
                opposite = input("Identifier inverse: ")
                inverses.append(opposite)
            synCheck = input("Would I know a synonym (y/n)?: ")
            while synCheck == "y":
                for i in self.network.nodeList:
                    print(i)
                newSyn = input("Enter match (or bad value to exit): ")
                if self.network.contains(newSyn):
                    synonyms.append(newSyn)
                    synCheck = input("Add another (y/n)?: ")
                else:
                    synCheck = "n"

            relatedWord = input("What is " + string + " related to?: ")
            finalAdd = self.linkWord(string, relatedWord)
            related.append(finalAdd)
            self.network.addNode(newAddition, [tenses, synonyms, related, inverses])
            print("Successfully linked " + str(newAddition) + " with " + finalAdd)

        else:
            newCheck = input("I already know " + string + ", teach a different word (y/n)?: ")
            if newCheck == "y":
                newAdd = input("What word am I learning?: ")
                correctCheck = input("You're about to teach " + newAdd + ", is this correct (y/n)?: ")
                while correctCheck == "n":
                    newAdd = input("What word am I learning?: ")
                    correctCheck = input("You're about to teach " + newAdd + ", is this correct (y/n)?: ")
                self.addWord(newAdd)

    def linkWord(self, potentialString, potentialLink):
        # branch into either a recursive add until a connection is found or add a connection to an already existing node
        if not self.network.contains(potentialLink):
            correctCheck = input("You're about to teach " + potentialLink + " as well, is this correct (y/n)?: ")
            while correctCheck == "n":
                potentialLink = input("What is " + potentialString + "related to?: ")
                correctCheck = input("You're about to teach " + potentialLink + ", is this correct (y/n)?: ")
            # recursive call back to addWord
            self.addWord(potentialLink)
            return potentialLink
        else:
            correctCheck = input("You're about to link " + potentialString + " to " + potentialLink + ", is this correct (y/n)?: ")
            while correctCheck == "n":
                potentialLink = input("What is " + potentialString + "related to?: ")
                if not self.network.contains(potentialLink):
                    #send back to the top
                    self.linkWord(potentialString, potentialLink)
                else:
                    correctCheck = input("You're about to teach " + potentialLink + ", is this correct (y/n)?: ")
            return potentialLink
















