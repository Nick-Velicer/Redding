import baseProcedureHandler as bph
handler = bph.BaseProcedureHandler()
handler.initializeNetwork("C:\\Redding\\data\\parsenetwork.json")
handler.network.print(-1)
word = input("Choose word: ")
handler.addWord(word)
handler.backupNetwork("C:\\Redding\\data\\parsenetwork.json")
handler.initializeNetwork("C:\\Redding\\data\\parsenetwork.json")
