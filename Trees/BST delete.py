# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: #found the value
            if not root.right:
                return root.left
            if not root.left:
                return root.right #if children is one
            
            temp = root.right #when have both children
            num = temp.val
            while temp.left:
                temp = temp.left
                num = temp.val
            root.val = num #replace number
            root.right = self.deleteNode(root.right, root.val)
        
        return root
