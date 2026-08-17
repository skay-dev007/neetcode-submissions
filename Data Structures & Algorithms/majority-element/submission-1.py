from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        counts = dict(Counter(nums))
        counts = list(counts.items())
        counts.sort(key = lambda x: x[1], reverse=True)
        return counts[0][0]
