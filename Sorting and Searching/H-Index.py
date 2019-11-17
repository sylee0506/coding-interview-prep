#Google Kick Start Round H 2019 #1 H-index
#This code is a version of same question in leetcode; #274.H-Index
#Time complexity: O(n) except sorting part

import sys

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        if len(citations) == 1:
            if citations[0] > 0:
                return 1
            else:
                return 0
            
        ans = 0
        tmp = sys.maxint
        citations.sort(reverse =True)
        
        for i in range(len(citations)):
            if i < citations[i] and ans < tmp:
                ans += 1
                tmp = min(tmp, citations[i])
        
        return ans
