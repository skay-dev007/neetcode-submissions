class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_char, t_char = [0]*26, [0]*26 
        if len(s) != len(t):
            return False 

        for char in s:
            index = ord(char) - 97
            s_char[index] += 1 
        
        for char in t: 
            index = ord(char) - 97 
            t_char[index] += 1 
        

        if s_char == t_char: 
            return True 
        else: 
            return False 
        
