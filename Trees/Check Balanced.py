#cracking the coding interview 4.4 (p110)
#check if binary tree is balanced or not
#depth of each subtree is the maximum depth of it; so just subtract min depth and max depth of tree would not work

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            
            left  = check(root.left)
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        
        if check(root) == -1:
            return False
        else:
            return True
