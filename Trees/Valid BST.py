#cracking the coding interview 4.5 (p110)
#determine if it is a valid BST
#used inorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.arr = []
        self.count = 0
        self.inorder(root)
        
        for i in range(len(self.arr)): #has duplicate
            if i+1 < len(self.arr):
                if self.arr[i] == self.arr[i+1]:
                    return False
                
        return self.arr == sorted(self.arr)

    def inorder(self, root):
        if root == None:
            return root
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
