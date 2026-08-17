class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        store = {}
        for index in range(len(numbers)):
            x = numbers[index]
            y = target - x
            if y in store:
                y_index = store[y]
                return [y_index+1, index+1]
            else:
                store[x] = index 
            
        