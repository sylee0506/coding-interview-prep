"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        bfs = [root]
        
        while bfs:
            arr = []
            for node in bfs:
                arr.append(node.val)
            ans.append(arr)
            
            temp = bfs
            bfs = []
            for node in temp:
                for child in node.children:
                    if child:
                        bfs.append(child)

        return ans
