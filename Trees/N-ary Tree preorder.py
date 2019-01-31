"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        
        stack = [root]
        ans = []
        
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            stack.extend(reversed(cur.children))
        
        return ans
