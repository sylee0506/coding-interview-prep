#implement hash map(hash table) using only arrays, without using any built-in hash table libraries
#used linked list ; hash with chaining
#put(), get(), remove()

class listNode:
    def __init__(self,key,value):
        self.pair = (key,value)
        self.next = None
        
class MyHashMap:        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.arr = [None]*1000000 //these are what I did first, it worked but not professional and slow
        
        self.m = 1000
        self.slot = [None]*self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        #self.arr[key] = value
        
        index = key % self.m
        if self.slot[index] == None:
            self.slot[index] = listNode(key,value) #new node
        else:
            curNode = self.slot[index]
            while True:
                if curNode.pair[0] == key:
                    curNode.pair = (key,value) #update / can't only change value because it's tuple
                    return
                
                if curNode.next == None:
                    break
                curNode = curNode.next
            
            curNode.next = listNode(key,value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        #if self.arr[key] != None:
        #    return self.arr[key]
        #else:
        #    return -1
        
        index = key % self.m
        if self.slot[index] != None:
            curNode = self.slot[index]
        else:
            return -1
        
        while True:
            if curNode.pair[0] == key:
                return curNode.pair[1] #return value
            
            if curNode.next == None:
                return -1
            curNode = curNode.next
                

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        #self.arr[key] = None
        
        index = key % self.m
        if self.slot[index] == None:
            return
        else:
            curNode = prev = self.slot[index]
        
        if curNode.pair[0] == key:
            self.slot[index] = curNode.next
        else:
            while True:
                if curNode.pair[0] == key:
                    prev.next = curNode.next
                    curNode = prev
                    return
                
                if curNode.next == None:
                    return
                prev = curNode
                curNode = curNode.next
                
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
clean linked list code)

def __init__(self):
        self.m = 1000;
        self.h = [None]*self.m
        

    def put(self, key, value):
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next
"""
