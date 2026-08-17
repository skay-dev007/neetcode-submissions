class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #transpose 
        # upper triange loop 
        # all rows but col > row 
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #flip along column ie y axis 
        # run till mid of cols 
        # all rows 
        max_col = len(matrix[0]) - 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j], matrix[i][max_col - j] = matrix[i][max_col -j], matrix[i][j]
        

     
