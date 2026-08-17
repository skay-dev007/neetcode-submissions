class Solution:
    def myPow(self, x: float, n: int) -> float:


        def recur(x,power):
            if power == 0:
                return 1 
            
            if x == 0:
                return 0 
            
            res = recur(x, power//2)
            res = res * res 
            return res * x if power%2 else res 
        
        return recur(x,n) if n>= 0 else 1/recur(x,-n)
        