#cracking the coding interview 2.2 (p94)
#return Kth largest element; since the main purpose is to sort linked list, solved sorting problem in leetcode
#time complexity: mergesort; O(nlogn)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if not head or not head.next:
            return head
        
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre, slow, fast =slow, slow.next, fast.next.next #slow becomes middle node of list
        pre.next = None
        
        return self.mergeSort(self.sortList(head), self.sortList(slow))
    
    def mergeSort(self, n1, n2):
        ret = dummy = ListNode(None)
        
        while n1 and n2:
            if n1.val < n2.val:
                dummy.next, dummy, n1 = n1, n1, n1.next
            else:
                dummy.next, dummy, n2 = n2, n2, n2.next
            
        dummy.next = n1 or n2
        return ret.next
