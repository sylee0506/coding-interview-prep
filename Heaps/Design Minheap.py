#to implement max heap, change < or >
#time complexity: approximately O(logn)

class binHeap:
    def __init__(self):
        self.heapList = [0] #to use child = 2*parent / 2*parent + 1 relation, put dummy in 0 index
        self.size = 0

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1

        temp = self.size
        while temp // 2:
            if self.heapList[temp] < self.heapList[temp//2]:
                self.heapList[temp], self.heapList[temp//2] = self.heapList[temp//2], self.heapList[temp]
            temp = temp // 2

    def extractMin(self):
        ret = self.heapList[1] #index 0 is dummy data
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1 #swap min(=root) and last element

        temp = 1
        while 2*temp <= self.size: #swap until last level
            target = self.minChild(temp)
            if self.heapList[temp] > self.heapList[target]:
                self.heapList[temp], self.heapList[target] = self.heapList[target], self.heapList[temp]
            temp = target

    def minChild(self, i):
        if 2*i + 1 > self.size:
            return 2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i + 1]:
                return 2*i
            else:
                return 2*i + 1
        
#testing
myheap = binHeap()
myheap.insert(5)
myheap.insert(9)
myheap.insert(14)
myheap.insert(27)
myheap.insert(7)
myheap.insert(11)
print(myheap.heapList)
myheap.extractMin()
print(myheap.heapList)

myheap.insert(5)
myheap.insert(6)
myheap.insert(2)
print(myheap.heapList)
myheap.insert(3)
myheap.extractMin()
print(myheap.heapList)
myheap.extractMin()
print(myheap.heapList)
