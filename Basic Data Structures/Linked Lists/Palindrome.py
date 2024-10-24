#cracking the coding interview 2.6 (p95)
#determine if singly linked list is palindrome or not
#time complexity: O(n) / space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt #reverse list after middle node
        
        while node:
            if head.val != node.val:
                return False
            else:
                head = head.next
                node = node.next
        return True
