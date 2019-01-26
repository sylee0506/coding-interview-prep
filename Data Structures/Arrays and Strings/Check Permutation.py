#cracking the coding interview 1.2 (p90)
#write a function to return true if (string) s2 contains the permutation of s1
#sliding window algorithm : O(n)

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
