class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1, len2 = len(word1), len(word2) 
        merged = []
        ptr1, ptr2 = 0,0 

        while ptr1 < len1 and ptr2 < len2: 
            merged.append(word1[ptr1]) 
            merged.append(word2[ptr2])
            ptr1+= 1 
            ptr2+= 1 
        
        merged.append(word1[ptr1:])
        merged.append(word2[ptr2:])
        

        return "".join(merged)





        