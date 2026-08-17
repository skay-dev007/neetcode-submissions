class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        curr = n 
        while curr:
            digits = [int(char)**2 for char in str(curr)]
            total = sum(digits)

            if total == 1:
                return True 
            elif total in seen:
                return False 
            else:
                seen.add(total)
            
            curr = total 
            
            


        