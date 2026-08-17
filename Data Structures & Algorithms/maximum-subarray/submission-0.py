class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #what do you want to do
        #mark the first element as largest 
        # keep adding next element if next element sum is greater than or equal to maxsum continue and update 
        # else exclude and take just value at index 
        # if max(total + curr, curr) 


        maxsum, currsum = nums[0], 0 
     
        for num in nums:
            currsum = max(currsum + num,num)
            if currsum > maxsum:
                maxsum = currsum

        return maxsum  



        