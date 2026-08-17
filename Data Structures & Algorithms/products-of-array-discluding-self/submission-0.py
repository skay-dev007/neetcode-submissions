class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        left_prod_arr,right_prod_arr = [1]*len(nums), [1]*len(nums)

        prod = nums[0]
        for element_index in range(1,len(nums)):
            left_prod_arr[element_index] = prod 
            prod *= nums[element_index]
        
        prod = nums[-1]
        for element_index in range(len(nums)-2,-1,-1):
            right_prod_arr[element_index] = prod
            prod *= nums[element_index]
      
        result = []
        for element_index in range(len(nums)):
            res = left_prod_arr[element_index] * right_prod_arr[element_index]
            result.append(res)
    
        return result



        