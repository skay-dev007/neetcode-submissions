class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        elements = {}
        curr_max = 0 
        nums.sort()
        for num in nums: 
            elements[num] = elements.get(num-1,0) + 1 
            if curr_max < elements[num]: 
                curr_max = elements[num]
        
        return curr_max 
        