from hashFunctions import hashFunction

fileName = 'ArchNombres1.txt'
myFile = open(fileName, 'r', encoding='utf-8')
myHashDict = {i:(None,None) for i in range(103)}


def insertHashTable(hashValue, number, name):

    if ( myHashDict[hashValue][0] == None):
        myHashDict[hashValue] = (number,name)
        return
    else:
        while(myHashDict[hashValue][0] != None ):
            a=hashValue
            jump = 1
            hashValue = a + (jump)**2 
            if (hashValue >= 102):
                hashValue -= 102
            insertHashTable(hashValue, number, name)
            jump+=1
            return 

def contains(number):
  hashValue=hashFunction(number)
  if (myHashDict[hashValue][0] == number):      
    return (hashValue, myHashDict[hashValue][0], myHashDict[hashValue][1])
  else:
    while(myHashDict[hashValue][0] != None ):
            a=hashValue
            jump = 1
            hashValue = a + (jump)**2 
            if (hashValue >= 102):
                hashValue -= 102
            if myHashDict[hashValue][0] == number:
                
                return (hashValue, myHashDict[hashValue][0], myHashDict[hashValue][1])
            jump+=1
    return "Identificacion no encontrada"
    

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

print(contains(565))