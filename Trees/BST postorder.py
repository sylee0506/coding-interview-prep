# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.postorder(root)
        
        return self.ans
    
    def postorder(self, root):
        if not root:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)
