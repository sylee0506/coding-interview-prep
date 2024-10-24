#cracking the coding interview 1.9 (p91)
#check if B is a rotation of A (rotation: shift leftmost char to rightmost position)
#time complexity: O(n) / space complexity: O(1)

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        
        for i in range(len(A)):
            if A == B:
                return True
            else:
                A = A + A[0]
                A = A[1:] # in one line) A = A[1:] + A[0]
        return False
