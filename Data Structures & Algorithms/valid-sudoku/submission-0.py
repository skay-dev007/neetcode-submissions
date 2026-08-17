class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check all rows
        for row in range(9):
            elements = set()
            for col in range(9):
                if board[row][col] != ".":
                    digit = int(board[row][col])
                    if digit in elements:
                        return False 
                    else:
                        elements.add(digit)
        #check cols 
        for col in range(9):
            elements = set()
            for row in range(9):
                if board[row][col] != ".":
                    digit = int(board[row][col])
                    if digit in elements:
                        return False 
                    else:
                        elements.add(digit)
        
        #check boxes
        for box in range(9):
            rowadd = (box // 3)*3 
            coladd = (box % 3) * 3 
            elements = set()
            for row in range(3):
                for col in range(3):
                    if board[row+rowadd][col+coladd] != ".":
                        digit = int(board[row+rowadd][col+coladd])
                        if digit in elements:
                            return False 
                        else:
                            elements.add(digit)
        
        return True 



        

        

            
                


        