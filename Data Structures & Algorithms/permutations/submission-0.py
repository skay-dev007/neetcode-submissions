class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # recursive, loop level
        # an array left after removing specific elements 

        self.res = []

        def ugh(curr_path,remaining_array):
            if len(curr_path) == len(nums):
                self.res.append(curr_path[:])
                return 
            
            for index in range(len(remaining_array)):
                curr_path.append(remaining_array[index])
                ugh(curr_path,remaining_array[:index]+remaining_array[index+1:])
                curr_path.pop()
        
        ugh([],nums[:])
        return self.res




        