class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top,bottom = 0,len(matrix) - 1
        left,right = 0, len(matrix[0]) - 1 

        spiral = []

        while top <= bottom and left <= right:

            for index in range(left,right+1):
                spiral.append(matrix[top][index])
            top += 1 

            for index in range(top,bottom+1):
                spiral.append(matrix[index][right])
            right -= 1 

            if not (left<= right and top <= bottom):
                break

            for index in range(right,left-1,-1):
                spiral.append(matrix[bottom][index])
            
            bottom -= 1 

            for index in range(bottom,top-1,-1):
                spiral.append(matrix[index][left])

            left += 1 
        
        return spiral 



        