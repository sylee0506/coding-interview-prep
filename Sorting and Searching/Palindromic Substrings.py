#Count how many palindromic substrings in this string
#Different start indexes or end indexes are counted as different substrings
#time complexity: O(n^2)
'''
idea:just search all cases; center of palindromic substring can be
    s[0], btw s[0] and s[1], s[1], btw s[1] and s[2]...
'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        ans = 0
        
        for i in xrange(2 * len(s) - 1):
            left = i / 2
            right = left + i % 2
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        
        return ans
