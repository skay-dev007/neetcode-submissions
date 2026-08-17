class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, (rows * cols) - 1

        while left <= right:

            m = left + (right - left) // 2 
            r, c = m // cols , m % cols 

            if target < matrix[r][c]:
                right = right - 1  
            
            elif target > matrix[r][c]:
                left = left + 1 
            
            else:
                return True 
        
        return False 




        
        