from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = sorted(Counter(nums).items(),key = lambda x: x[1], reverse=True)
        return freq[0][0] 
    


        