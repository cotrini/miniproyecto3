#this file contains all functions related to hash methods

#Hash Function based on % mod operator, in a id from a person and hashTableSize this parameter is selected from Gui
def hashFunction(id, hashTableSize):
    return id % hashTableSize

def fileWriter(myHashDict : dict):
    fileName = 'dataset.txt'
    myFile = open(fileName, 'w', encoding='utf-8')
    for key in myHashDict:
        myFile.write(str(key)+';'+str(myHashDict[key][0])+';'+str(myHashDict[key][1])+'\n')

#Insert to hash table function, write on a file the hash Value, original position on file like a tuple and return amounth of collisions to write a simple value
def insertHashTable(idList:list, hashTableSize):
    myHashDict = {i:(None,None) for i in range(hashTableSize)}
    collisions = 0
    for id in idList:
        hashValue = hashFunction(id,hashTableSize)
        if ( myHashDict[hashValue][0] == None):
            myHashDict[hashValue] = (id,idList.index(id))
        else:
            collisions += 1
            a=hashValue
            jump = 1
            while(myHashDict[hashValue][0] != None ):
                hashValue = hashFunction((a + (jump)**2 ), hashTableSize)
                if (hashValue >= hashTableSize):
                    hashValue -= hashTableSize
                jump+=1
            myHashDict[hashValue] = (id, idList.index(id))
    fileWriter(myHashDict)
    return collisions

# this Function contains, return information of a person by his id, and 

def contains(id, hashTableSize):
    namesDatabase = open('ArchNombres1.txt', encoding='utf-8').readlines()
    datasetFile = open('dataset.txt',encoding='utf-8').readlines()
    hashValue=hashFunction(id, hashTableSize)
    if ( int(datasetFile[hashValue].split(';')[1]) == id):      
        return (hashValue, namesDatabase[int(datasetFile[hashValue].split(';')[2])].split(',')[0], namesDatabase[int(datasetFile[hashValue].split(';')[2])].split(',')[1])
    else:
        a=hashValue
        jump = 1
        while(datasetFile[hashValue].split(';')[1] != 'None' ):
                hashValue = hashFunction((a + (jump)**2),hashTableSize)
                if (hashValue >= hashTableSize):
                    hashValue -= hashTableSize
                try:
                    if (int(datasetFile[hashValue].split(';')[1]) == id):
                        return (hashValue, namesDatabase[int(datasetFile[hashValue].split(';')[2])].split(',')[0], namesDatabase[int(datasetFile[hashValue].split(';')[2])].split(',')[1])
                except:
                    pass
                jump+=1
        return "0"