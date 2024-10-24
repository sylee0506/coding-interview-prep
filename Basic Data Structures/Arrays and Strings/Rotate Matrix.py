#cracking the coding interview 1.7 (p91)
#rotate n*n 2D matrix image by 90 degrees (clockwise)
#time complexity : (n^2) (n/2 * n/2) / space complexity : O(1) 

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        for i in range(n-1):
            for j in range(n-1):
                if j == n-1-i:
                    break
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = temp #swap symmetry ; matrix[i][j],matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i],matrix[i][j]
        
        matrix.reverse() #reverse up to down

"""
common method to rotate image)
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
"""

"""
python good code)
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:
            l.reverse()
"""
