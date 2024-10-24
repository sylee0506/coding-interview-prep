#cracking the coding interview 2.3 (p94)
#delete the middle node of a singly linked list
#time complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        size = 1
        ptr = head
        
        while True:
            if ptr.next == None:
                break
            
            ptr = ptr.next
            size += 1
        
        middle = size//2 + 1
        
        for i in range(middle-1):
            head = head.next
        
        return head

"""
***remeber to use fast & slow pointers in linked list!!

python good code)
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
"""
