class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        store = {}
        for x_index in range(len(nums)):
            x = nums[x_index]
            y = target - x 
            if y in store:
                y_index = store.get(y)
                return [y_index,x_index]
            store[x] = x_index
        



        