from copy import deepcopy 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        final = [[]]

        for i in range(len(nums)):
            curr = deepcopy(final)
            for ele in curr:
                updated = ele + [nums[i]] 
                final.append(updated)
        
        return final
        