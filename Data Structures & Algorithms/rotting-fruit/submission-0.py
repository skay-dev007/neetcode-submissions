from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        R, C = len(grid), len(grid[0])
        queue = deque()

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    queue.append((row,col)) 

        minute = 0 
        while queue:
            length = len(queue)
            for ele in range(length):
                r,c = queue.popleft()
                neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
                for x,y in neighbors:
                    nr,nc = r+x, y+c

                    if nr < R and nc < C and nr >= 0 and nc >= 0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        queue.append((nr,nc))             
            if queue:
                minute += 1 
        

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    return -1 
        
        return minute
                






        