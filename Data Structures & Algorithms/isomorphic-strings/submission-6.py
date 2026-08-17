from collections import Counter 
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        match = {}

        for i,char in enumerate(s):
            if char in match: 
                matched = match[char]
                if matched != t[i]:
                    return False 
            else: 
                match[char] = t[i] 

        match = {}
        for i,char in enumerate(t):
            if char in match: 
                matched = match[char]
                if matched != s[i]:
                    return False 
            else: 
                match[char] = s[i] 

        
        return True 
        