#cracking the coding interview 3.4 (p99)
#implement queue using two stacks
#push:O(1)/pop&peek:O(n) => O(n)


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.flag = 0

        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x) #push into first stack
        self.flag = 0

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.flag == 0:
            self.moveAll() #move elements of first stack to second stack from top -> reversed
        
        self.flag = 1
        del self.s1[0] #also pop from first stack
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.flag == 0:
            self.moveAll()
        
        self.flag = 1           
        return self.s2[len(self.s2)-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.flag == 0:
            return self.s1 == []#when pop/peek not happens
        else:
            return self.s2 == []
    
    def moveAll(self):
        self.s2 = []
        top = len(self.s1) - 1
        for i in range(len(self.s1)):
            self.s2.append(self.s1[top])
            top -= 1
    
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
