import multiRelationalNetwork as mrn

readData = []
with open("testFile.txt") as file:
    readData = [line.rstrip() for line in file]

#formatting input data for function calls
#assumes single character value and single character weight
for i in range(len(readData)):
    readData[i] = readData[i].split(" ", 1)
    #print(readData[i])
    holderList = []
    j = 0
    while j < len(readData[i][1]):
        if readData[i][1][j] != "[":
            while readData[i][1][j] != "]":
                holderList.append([readData[i][1][j], readData[i][1][j+2]])
                j+=4
            j+=2
        else:
            j+=1

    readData[i][1] = holderList


print("Input Data:")
print(readData)
print()


testMRN = mrn.MRN(len(readData[i][1]))
#adding nodes
for i in range(len(readData)):
    #print("Calling addNode("+ readData[i][0] +", "+str(readData[i][1]))
    testMRN.addNode(readData[i][0], readData[i][1])

print()
print("MRN Initialized:")
testMRN.print()

#removing nodes
i = 0
while i < len(readData):
    testMRN.removeNode(readData[i][0])
    i+= 2

print("Nodes Removed:")
testMRN.print()

#adding edges
testMRN.addEdge("B", "D", 1, 0)
testMRN.addEdge("D", "E", 8, 1)
print("Edges Added: ")
testMRN.print()

testMRN.removeEdge("B", "D", 0)
testMRN.removeEdge("E", "D", 1)
print("Edges Removed: ")
testMRN.print()

