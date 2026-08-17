
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = dict(Counter(nums))
        pairs = list(counts.items()) 
        pairs.sort(key=lambda x: x[1],reverse=True)  

        return [k for (k,v) in pairs[:k]]
         






        