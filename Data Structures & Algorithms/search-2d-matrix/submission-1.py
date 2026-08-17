class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 

        low, high = 0,len(matrix) -1 

        while low <= high:

            midrow = (low + high) // 2

            if target < matrix[midrow][0]:
                high = midrow - 1 

            elif target > matrix[midrow][-1]:
                low = midrow + 1 
            else:
                break 

        if low > high:
            return False         

        low,high = 0, len(matrix[0])

        while low<= high:

            mid = (low + high) // 2 

            if matrix[midrow][mid] == target:
                return True 
            elif matrix[midrow][mid] < target:
                low = mid + 1 
            
            else:
                high = mid - 1  
              

        
        return False 





