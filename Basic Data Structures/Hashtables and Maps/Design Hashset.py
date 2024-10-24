#implement hash map(hash table) using only arrays, without using any built-in hash table libraries
#used linked list ; hash with chaining
#add(), remove(), contains()

class listNode:
    def __init__(self,key):
        self.key = key
        self.next = None
        
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.slot = [None]*self.m
    
    def myHash(self, key):
        return key % self.m

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.myHash(key)
        if self.slot[index] == None:
            self.slot[index] = listNode(key)
            return
        else:
            curNode = self.slot[index]
        
        while True:
            if curNode.key == key:
                return
            
            if curNode.next == None:
                break
            curNode = curNode.next
            
        curNode.next = listNode(key)          

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        index = self.myHash(key)
        if self.slot[index] == None:
            return
        else:
            curNode = prev = self.slot[index]
        
        if curNode.key == key:
            self.slot[index] = curNode.next
        else:
            while curNode:
                if curNode.key == key:
                    prev.next = curNode.next
                    return
            
                prev = curNode
                curNode = curNode.next
                
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = self.myHash(key)
        if self.slot[index] == None:
            return False
        else:
            curNode = self.slot[index]
        
        while curNode:
            if curNode.key == key:
                return True
            
            curNode = curNode.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
