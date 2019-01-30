# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        
        return []

"""
my another solution ; recursion)
class Solution:
    def searchBST(self, root, val):
        self.ans = []
        
        if not root:
            return
            
        if root.val == val:
            self.ans = root
        elif root.val < val:
            self.searchBST(root.right,val)
        elif root.val > val:
            self.searchBST(root.left,val)
        
        return self.ans
"""

"""
python other good code)
class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root
"""
