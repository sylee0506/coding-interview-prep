class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

"""
testing)
num1, num2 = input("input number:").split(' ')
num1 = int(num1); num2 = int(num2)
myQueue = Queue()
myQueue.enqueue(num1)
myQueue.enqueue(num2)
myQueue.dequeue()
print(myQueue.size())
print(myQueue.isEmpty())
print(myQueue.dequeue())
print(myQueue.isEmpty())
"""
    
