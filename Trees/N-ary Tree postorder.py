"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            stack.extend(cur.children)
        
        return list(reversed(ans))
