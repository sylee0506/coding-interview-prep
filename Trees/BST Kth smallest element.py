# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.arr = []
        self.inorder(root,k)
        
        return self.arr[k-1]
        
    def inorder(self, root,k):
        if root == None:
            return
        
        self.inorder(root.left,k)
        self.arr.append(root.val)
        self.inorder(root.right,k)

"""
python iterative good code)
def kthSmallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
"""
