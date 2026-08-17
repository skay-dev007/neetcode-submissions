from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
        
        left,right = 0,len(s1)-1 

        while left <=right and right<len(s2):
            if Counter(s2[left:right+1])  == Counter(s1):
                return True 
            left+=1 
            right+=1 

        return False  



        



        