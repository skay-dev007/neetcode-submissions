class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9): 
            row_nums = set()
            col_nums = set()
            for col in range(9): 
                if board[row][col] in row_nums and board[row][col] != ".":
                    return False 
                else: 
                    row_nums.add(board[row][col])

                if board[col][row] in col_nums and board[col][row] != ".":
                    return False 
                else: 
                    col_nums.add(board[col][row]) 
                
         
        

        for grid_row in range(0,9,3):
            for grid_col in range(0,9,3):
                grid_nums = set() 
                for row in range(3):
                    for col in range(3): 
                        if board[grid_row+row][grid_col +col] in grid_nums and board[grid_row+row][grid_col +col]!=".":
                            return False 
                        else: 
                            grid_nums.add(board[grid_row+row][grid_col +col])
        

        return True 



        