class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helpercheck(l,r):

            while l<r: 
                if s[l] != s[r]:
                    return False 
                l+=1 
                r-= 1 
            
            return True 

        
        start, end = 0,len(s) -1 

        while start < end: 
            if s[start] != s[end]:
                return helpercheck(start+1,end) or helpercheck(start,end-1) 
            
            start += 1
            end -= 1 
        
        return True 

        