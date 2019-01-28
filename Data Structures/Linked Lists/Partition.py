#cracking the coding interview 2.4 (p94)
#partition a linked list such that all nodes less than x come before nodes greater than or equal to x
#time complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ptr = prev = head
        while ptr:
            if ptr.val >= x:
                break
            prev = ptr
            ptr = ptr.next
        
        fast = ptr
        slow = prev
        while fast:
            if fast.val < x:
                new = ListNode(fast.val)
                if ptr == head: #insert in front, also means prev is head
                    new.next = ptr
                    head = prev = new
                else:
                    new.next = ptr
                    prev.next = new 
                    prev = new #insert node
                
                slow.next = fast.next
                fast = slow #delete node
                
            slow = fast
            fast = fast.next
        
        return head

"""
python good code)
#h1 becomes list of values smaller than x, h2 becomes list of values bigger thas x or same as x

def partition(self, head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next
"""
