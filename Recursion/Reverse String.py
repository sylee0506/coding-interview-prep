class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)/2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1],s[i]
        
        #self.helper(s, 0, len(s)-1)
    
    #def helper(self, s, i, j):
        #if i >= j:
            #return
        #s[i], s[j] = s[j], s[i]
        #self.helper(s, i+1, j-1)

#recursion worked, but slower and used more memory
