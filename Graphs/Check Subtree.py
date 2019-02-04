#cracking the coding interview 4.10 (p111)
#check if t is subtree of s
#search two tree by DFS

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == t == None:
            return True
        elif (not s and t) or (not t and s):
            return False
        
        if s.val == t.val and self.check(s, t):
            return True
        
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def check(self, s, t):
        if not s and not t:
            return
        elif (not s and t) or (s and not t):
            return False
        
        if s.val != t.val:
            return False
        
        left = self.check(s.left, t.left)
        right = self.check(s.right, t.right)
        
        if left == False or right == False:
            return False
        else:
            return True

"""
python good code ; convert into string)
class Solution(object):
    def isSubtree(self, s, t):
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"        
        return convert(t) in convert(s)
"""
