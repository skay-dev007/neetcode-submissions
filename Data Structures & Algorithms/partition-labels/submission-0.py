from collections import Counter 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        counts = Counter(s)
        letters = set()
        results = []
        length = 0 
        for index in range(len(s)):
            if counts[s[index]] >= 1:
                length += 1 
                counts[s[index]] -=1. 
                if s[index] not in letters:
                    letters.add(s[index])
            if counts[s[index]] == 0:
                letters.remove(s[index]) 
            
            if not letters:
                results.append(length)
                length = 0

        return results    


        