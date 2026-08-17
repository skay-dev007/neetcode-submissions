from collections import Counter 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_start, t_start = 0, 0 

        while s_start < len(s) and t_start < len(t):

            if s[s_start] == t[t_start]:
                s_start += 1 
            t_start += 1 
           
        

        return s_start == len(s)
         


        