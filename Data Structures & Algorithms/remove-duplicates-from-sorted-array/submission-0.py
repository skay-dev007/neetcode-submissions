class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left, right = 0, 1
        count = 1 

        while right < len(nums):

            if nums[left] == nums[right]:
                right += 1 
            else:
                if right - left > 1:
                    nums[left+1] = nums[right]
                left += 1                     
                count += 1 



        return count 
        