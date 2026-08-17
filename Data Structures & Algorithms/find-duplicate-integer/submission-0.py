class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow,fast = 0,0 

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 

        
        slow_two = 0 
        while slow_two != slow:
            slow_two = nums[slow_two]
            slow = nums[slow]
        
        return slow 