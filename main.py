from hashFunctions import hashFunction

fileName = 'ArchNombres1.txt'
myFile = open(fileName, 'r')
myHashDict = {i:(None,None) for i in range(103)}


def insertHashTable(hashValue, number, name):

    if ( myHashDict[hashValue][0] == None):
        myHashDict[hashValue] = (number,name)
        return
    else:
        while(myHashDict[hashValue][0] != None ):
            jump = 1
            if (hashValue >= 102):
                hashValue -= 102
            hashValue += jump * 2
            insertHashTable(hashValue, number, name)
            return 


for element in myFile: 
    number = int(element.split(',')[0])
    name = element.split(',')[1]
    hashValue = hashFunction(number)
    insertHashTable(hashValue,number,name)


counter = 0
for key in myHashDict:
    if (myHashDict[key][0] == None):
        counter += 1
    print(key,' ',myHashDict[key])

print(counter)

