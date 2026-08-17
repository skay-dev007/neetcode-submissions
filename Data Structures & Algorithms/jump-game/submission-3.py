
class Solution:
    def canJump(self, nums: List[int]) -> bool:


        #how will the loop end? 
        # if the element encounterd is 0 it won't move 
        # if the jump goes beyond len of array then also won;t work 
        
        # recursion
        # r(0) -> r (1) -> r(2) -> r
        self.cheatcode = False 
        def recurse(curr_index):
            if curr_index == len(nums) - 1:
                self.cheatcode = True
            if curr_index >= len(nums):
                return  
            
            for step in range(1,nums[curr_index]+1):
                print(curr_index+step)
                recurse(curr_index+step)
                
        recurse(0)
        return self.cheatcode 

            

            


        