#cracking the coding interview 3.2 (p98)
#design a stack which functions push,pop,top,and returning min value
#use 2D array, store pushed value in index 0, store min vlaue in index 1 => O(1)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.s == []:
            self.s.append((x,x))
        else:
            min_val = self.s[-1][1]
            self.s.append((x,min(x,min_val)))

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.s[len(self.s)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[len(self.s)-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
