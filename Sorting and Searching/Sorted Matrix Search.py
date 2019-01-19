#cracking the coding interview 10.9 (p151)
#algorithm that searches for a value in an m x n matrix ; each row and column is sorted in ascending order
#mine : worst case O(mn) ; use binary search -> O(logn) (code below)


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if target <= matrix[i][n-1]:
                break
        
        for j in range(n):
            if target == matrix[i][j]:
                return True
        
        return False

'''
binary search code) O(logn)

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # 8:21
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
'''
