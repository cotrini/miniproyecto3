class BinaryHeap():

    def __init__(self):
       self.heapList = [(0, 0)]
       self.currentSize = 0

    def insert(self, k, index):
        self.heapList.append((k, index))
        self.currentSize += 1
        self.percUp(self.currentSize)

    def findMin(self):
        return self.heapList[1]

    def isEmpty(self):
        return not bool(self.heapList)

    def buildHeap():
        pass

    def minChild(self, i):
        if((i * 2 + 1) > self.currentSize):
            return i * 2
        else:
            if(self.heapList[i*2][0]< self.heapList[i*2+1][0]):
                return i * 2
            else:
                return i * 2 + 1

    def percUp(self, i):
        while ( i // 2 > 0):
            if(self.heapList[i][0] < self.heapList[i // 2][0]):
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def percDown(self, i):
        while((i * 2) <= self.currentSize):
            mc = self.minChild(i)
            if(self.heapList[i][0]>self.heapList[mc][0]):
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def getTenRegisters(self):
        tenList = []
        for i in range(10):
            tenList.append(self.delMin())
        return tenList

