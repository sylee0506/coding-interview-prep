#cracking the coding interview 1.8 (p91)
#given a m x n matrix, if an element is 0, set its entire row and column to 0
#time complexity: O(n^3) / space complexity: O(1) 

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    for h in range(m):
                        if matrix[h][j] != None:
                            matrix[h][j] = 0
                    for k in range(n):
                        if matrix[i][k] != None:
                            matrix[i][k] = 0
                            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0

"""
python another code)
#time complexity is O(mn), but space complexitiy is O(m+n)

class Solution(object):
    def setZeroes(self, matrix):        
        row = len(matrix)
        col = len(matrix[0])
        
        r = [None]*row
        c = [None]*col
        
        i, j = 0, 0
        
        for i in xrange(row):
            for j in xrange(col):
                if matrix[i][j] == 0:
                    r[i] = 0
                    c[j] = 0
        
        for i in xrange(len(r)):
            for j in xrange(len(c)):
                if r[i] == 0 or c[j] == 0:
                    matrix[i][j] = 0
"""
