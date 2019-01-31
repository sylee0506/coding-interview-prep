# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        self.ans = []
        self.inorder(root)
        
        return self.ans
    
    def inorder(self, root):
        if root == None:
            return
    
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right) #recursive code
        """
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            ans.append(root.val)
            root = root.right #iterative code, using stack, more faster
        
        return ans
