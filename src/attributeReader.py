# Nick Velicer, 8/23
# a miniature API to read from the attribute file
# read into a local JSON in the future instead of an array?

import os
import json

class AttributeReader():

    read = "empty json object"
    fileName = "empty file path"
    tempDict = {}

    def __init__(self, name):
        self.fileName = name

    def add(self, key, value):
        self.tempDict = {key: value}
        with open(self.fileName) as file:
            self.read = json.load(file)
            #getting 'name' from C:stuff/stuff/name.json
            obj = self.read[os.path.splitext(os.path.basename(os.path.normpath(self.fileName)))[0]]
            obj.append(self.tempDict)
            file.close()
        with open(self.fileName, "w") as file:
            json.dump(self.read, file, indent=4)
            file.close()

    def read(self):
        with open(self.fileName, "r") as file:
            self.read = json.load(file)
            file.close()
        return self.read

    def remove(self, key):
        with open(self.fileName) as file:
            self.read = json.load(file)
            #getting 'name' from C:stuff/stuff/name.json
            obj = self.read[os.path.splitext(os.path.basename(os.path.normpath(self.fileName)))[0]]
            deleteIndex = -1
            for i in range(len(obj)):
                if i.keys()[0] == key:
                    deleteIndex = i
                    break
            obj.pop(deleteIndex)
            file.close()
        with open(self.fileName, "w") as file:
            json.dump(self.read, file, indent=4)
            file.close()



