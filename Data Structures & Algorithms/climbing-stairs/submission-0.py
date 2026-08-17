class Solution:
    def climbStairs(self, n: int) -> int:

        # n = (n-1) + (n-2)
        # 1 -> 1 
        # 2 -> 1 + 1 or 2 
        # 3 -> 1 + 2 
        if n == 1 or n == 2:
            return n

        n_1, n_2 = 2,1
        curr = 0  

        for _ in range(3,n+1):
            curr = n_1 + n_2 
            n_2 = n_1 
            n_1 = curr 
        
        return curr 
            



        