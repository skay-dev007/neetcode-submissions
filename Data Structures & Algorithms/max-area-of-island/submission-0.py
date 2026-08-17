class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def grid_cover(row,col,r,c):

            if row<0 or col < 0 or row >= r or col >= c:
                return 

            if grid[row][col] == 1:
                grid[row][col] = 0 
                nonlocal curr_area
                curr_area += 1
                dirs = [(1,0), (-1,0), (0,1), (0,-1)]
                for x,y in dirs:
                    grid_cover(row+x,col+y,r,c) 

        max_area = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    curr_area = 0 
                    grid_cover(row, col,len(grid), len(grid[0])) 
                    if max_area < curr_area:
                        max_area = curr_area 
        
        return max_area 
        