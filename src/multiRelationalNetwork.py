#Nick Velicer, 8/19/22
class MRN:

    #an array of adjacency lists for all desired relations
    #individual adjacency list indices are formatted [[item, [adjacencies]], [item, [adjacencies]], ...]
    #adjacencies is an item/integer pair for weight
    nodeList = []
    adjacencyLists = []
    relationshipCount = 0

    def __init__(self, int):
        self.relationshipCount = int
        for i in range(int):
            self.adjacencyLists.append([])

    def __getitem__(self, key):
        return self.nodeList[key]

    def findItemIndex(self, item, selection):
        #returns the adjacency list index of an item, or -1 if it is not present
        #print("findItemIndex(" + str(item) + ", " + str(selection) + ")")
        currentList = self.adjacencyLists[selection]
        for i in range(len(currentList)):
            #print(str(currentList[i][0]) + " ?= " + str(item))
            if str(currentList[i][0]) == str(item):
                #print(str(currentList[i][0]) + " == " + str(item))
                return i
        return -1

    def addNode(self, item, adjacencies):
        #adjacencies is a list of adjacent lists for each relationship
        #item is the item to be added
        self.nodeList.append(item)
        if len(adjacencies) == 0:
            for i in range(self.relationshipCount):
                self.adjacencyLists[i].append([str(item), []])
        else:
            for i in range(self.relationshipCount):
                self.adjacencyLists[i].append([str(item), []])
                for j in range(len(adjacencies[i])):
                    if type(adjacencies[i][j]) == list:
                        self.addEdge(item, adjacencies[i][j][0], 0, i)
                    else:
                        self.addEdge(item, adjacencies[i][j], 0, i)


    def removeNode(self, item):
        #currently assumes item exists in the network
        #removing edge references
        #print("Removing node " + str(item))
        self.nodeList.remove(item)
        for i in range(self.relationshipCount):
            currentRelationship = self.adjacencyLists[i]
            #print("On Relationship "+ str(i))
            for j in range(len(currentRelationship)):
                if currentRelationship[j][0] != item:
                    #print("Current Adjacency List:")
                    currentAdjacencyList = currentRelationship[j][1]
                    #print(currentAdjacencyList)
                    for k in range(len(currentAdjacencyList)):
                        currentItem = currentAdjacencyList[k]
                        if currentItem[0] == item:
                            currentAdjacencyList.remove([currentItem[0], currentItem[1]])
                            break
        #removing the main node
        for i in range(self.relationshipCount):
            self.adjacencyLists[i].pop(self.findItemIndex(item, i))

    def addEdge(self, start, end, weight, selection):
        self.adjacencyLists[selection][self.findItemIndex(str(start), selection)][1].append([str(end), weight])

    def removeEdge(self, start, end, selection):
        currentList = self.adjacencyLists[selection][self.findItemIndex(start, selection)][1]
        for i in range(len(currentList)):
            if currentList[i][0] == end:
                currentList.remove([end, currentList[i][1]])
                break

    def updateWeight(self, start, end, selection, increment):
        for i in self.adjacencyLists[selection][self.findItemIndex(start, selection)][1]:
            if i[0] == end:
                i[1] += increment
                break

    def contains(self, title):
        for i in self.nodeList:
            if i.title == title:
                return True
        return False

    def size(self):
        return len(self.nodeList)

    def getEdges(self, item, selection):
        #return an unformatted collection of the adjacency lists in relationship order
        return self.adjacencyLists[selection][self.findItemIndex(item, selection)]

    #relationship you want to see (0 indexed)
    #-1 for all
    def print(self, relationship):
        #just print the nodes, matrices and indices, for debugging purposes
        print("Nodes: " + str(self.nodeList))
        print()
        if relationship < -1 or relationship > self.relationshipCount:
            print("Error: Bad range")
            return

        if relationship == -1:
            for i in range(self.relationshipCount):
                print("Relationship " + str(i) + ":")
                for j in range(len(self.adjacencyLists[i])):
                    print(self.adjacencyLists[i][j])
                print()
        else:
            for i in range(relationship):
                print("Relationship " + str(i) + ":")
                for j in range(len(self.adjacencyLists[i])):
                    print(self.adjacencyLists[i][j])
                print()

