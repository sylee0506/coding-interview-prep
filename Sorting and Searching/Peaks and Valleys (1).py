#cracking the coding interview 10.11 (p151)
#find peak element in array
#brutal force O(n)

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        flag = 0
        
        for i in range(len(A)):
            if flag == 0 and A[i] < A[i+1]:
                flag = 1
                continue
            
            if flag == 1 and A[i] > A[i+1]:
                return i
            elif flag == 1 and A[i] >= A[i+1]:
                flag = 0
