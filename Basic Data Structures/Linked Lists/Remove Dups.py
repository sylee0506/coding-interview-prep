#cracking the coding interveiw 2.1 (p94)
#remove duplicates from sorted list
#time complexity: O(n) / sapce complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return []
        
        fast = slow = head
        while fast.next:
            fast = fast.next
            if fast.val == slow.val:
                slow.next = fast.next
                fast = slow
            else:
                slow = slow.next
        return head
