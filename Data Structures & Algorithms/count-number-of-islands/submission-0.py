class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x,y):

            if x == len(grid) or y == len(grid[0]) or x <0 or y < 0 or grid[x][y] != '1':
                return 
            
            grid[x][y] = '.'
            neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx,dy in neighbors:
                x_ = x + dx
                y_ = y + dy
                dfs(x_,y_)
            
        
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == '1':
                    counter += 1 
                    dfs(row,col)

        return counter 
        
