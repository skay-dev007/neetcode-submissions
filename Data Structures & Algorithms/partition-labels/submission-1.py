from collections import Counter 
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {c:i for i,c in enumerate(s)}
        size = end = 0
        results = []

        for i,c in enumerate(s):
            end = max(end, last[c])
            size += 1 

            if i == end:
                results.append(size)
                size = 0

        return results
