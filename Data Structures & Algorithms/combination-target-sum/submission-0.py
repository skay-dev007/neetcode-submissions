class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #thinking of a recursive solution 
        # base case is that the sum goes over target or == target 
        # either we take the current number or don't 
        # 
        self.arr = set()
        def ugh(pos,curr_path):

            if pos == len(nums):
                return 
            if sum(curr_path)> target:
                return  
            if sum(curr_path) == target:
                self.arr.add(tuple(curr_path))
                return 
            
            ugh(pos+1,curr_path)
            curr_path.append(nums[pos])
            ugh(pos,curr_path)
            ugh(pos+1,curr_path)
            curr_path.pop() 

        ugh(0,[])
        return [list(ele) for ele in self.arr]