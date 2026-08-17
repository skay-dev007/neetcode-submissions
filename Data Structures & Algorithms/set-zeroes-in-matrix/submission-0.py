class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        R = len(matrix)
        C = len(matrix[0])

        is_col = False 

        for r in range(R):

            if matrix[r][0] == 0:
                is_col = True 
            
            for c in range(1,C):

                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0 
            
        
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0 

        if matrix[0][0] == 0:
            for c in range(C):
                matrix[0][c] = 0 
        
        if is_col:
            for r in range(R):
                matrix[r][0] = 0





        
        