# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        bfs = [root]
        ans = []
        
        while bfs:
            arr = []
            for node in bfs:
                if not node:
                    continue
                arr.append(node.val)
            
            temp = bfs
            bfs = []
            for node in temp:
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            
            ans.append(arr)
            
        return ans
