class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1, len2 = len(word1), len(word2) 
        min_len = min(len1,len2)
        merged = []
        ptr1, ptr2 = 0,0 

        while ptr1 < min_len or ptr2 < min_len: 
            if ptr1 == ptr2: 
                merged.append(word1[ptr1]) 
                ptr1+= 1 
            else:
                merged.append(word2[ptr2])
                ptr2+= 1 

        
        if ptr1 < len1: 
            while ptr1 < len1: 
                merged.append(word1[ptr1])
                ptr1+= 1
        elif ptr2 < len2:
            while ptr2 < len2:
                merged.append(word2[ptr2])
                ptr2+= 1
        

        return "".join(merged)





        