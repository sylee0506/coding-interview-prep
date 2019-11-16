#Google former coding interview question
#Let's paly minesweeper game!
#Leetcode #529.Minesweeper
#DFS method using recursion

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        clk_row = click[0]
        clk_col = click[1]
        ans = board
        
        if board[clk_row][clk_col] == "E":
            ans = self.revealEmptySquare(board, clk_row, clk_col)
        elif board[clk_row][clk_col] == "M":
            ans[clk_row][clk_col] = "X"
            
        return ans
    
    def checkNumMine(self, board, row, col):
        num_mine = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= row+i < len(board)) and (0 <= col+j < len(board[0])):
                    if board[row+i][col+j] == "M":
                        num_mine += 1

        return num_mine
        
    def revealEmptySquare(self, board, row, col):
        if board[row][col] != "E":
            return board
        
        ans = board
        num_mine = self.checkNumMine(board, row, col)
        if num_mine == 0:
            ans[row][col] = "B"
        else:
            ans[row][col] = str(num_mine)
            return ans
        
        '''
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= row+i < len(board)) and (0 <= col+j < len(board[0])):
                    ans = self.revealEmptySquare(board, row+i, col+j)
        '''
        #This took less time than just using for loop twice
        if row-1 >= 0:
            ans = self.revealEmptySquare(board, row-1, col)
            if col-1 >= 0:
                ans = self.revealEmptySquare(board, row-1, col-1)
            if col+1 < len(board[0]):
                ans = self.revealEmptySquare(board, row-1, col+1)
        if row+1 < len(board):
            ans = self.revealEmptySquare(board, row+1, col)
            if col-1 >= 0:
                ans = self.revealEmptySquare(board, row+1, col-1)
            if col+1 < len(board[0]):
                ans = self.revealEmptySquare(board, row+1, col+1)
        if col-1 >= 0:
            ans = self.revealEmptySquare(board, row, col-1)
        if col+1 < len(board[0]):
            ans = self.revealEmptySquare(board, row, col+1)

        return ans

'''
good code)
go through loop using directions array;
ex)
    directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
    for d in directions:
        ~~~~

+ BFS also available ; using queue 
'''
