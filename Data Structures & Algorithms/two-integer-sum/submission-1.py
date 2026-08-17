class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
        for idx,num in enumerate(nums):
            num_prev = target - num 
            if num_prev in store: 
                idx_prev = store[num_prev] 
                return [idx_prev, idx] 
            else:
                store[num] = idx 
        
        
        