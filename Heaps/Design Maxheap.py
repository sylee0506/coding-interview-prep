class binHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1

        temp = self.size
        while temp // 2:
            if self.heapList[temp] > self.heapList[temp//2]:
                self.heapList[temp], self.heapList[temp//2] = self.heapList[temp//2], self.heapList[temp]
            temp = temp // 2

    def extractMax(self):
        ret = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1

        temp = 1
        while temp*2 <= self.size:
            target = self.maxChild(temp)
            if self.heapList[temp] < self.heapList[target]:
                self.heapList[temp], self.heapList[target] = self.heapList[target], self.heapList[temp]
            temp = target

    def maxChild(self, i):
        if i*2 + 1 > self.size:
            return i*2
        else:
            if self.heapList[i*2] > self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1


#testing
myheap = binHeap()
myheap.insert(5)
myheap.insert(9)
myheap.insert(14)
myheap.insert(27)
myheap.insert(7)
myheap.insert(11)
print(myheap.heapList)
myheap.extractMax()
print(myheap.heapList)

myheap.insert(5)
myheap.insert(6)
myheap.insert(2)
print(myheap.heapList)
myheap.insert(3)
myheap.extractMax()
print(myheap.heapList)
myheap.extractMax()
print(myheap.heapList)
