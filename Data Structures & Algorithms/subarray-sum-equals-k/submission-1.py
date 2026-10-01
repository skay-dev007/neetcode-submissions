class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int: 

        seen = {0:1}
        prefix_sum = 0
        count = 0

        for num in nums: 
            prefix_sum += num 

            need = prefix_sum - k 

            if need in seen: 
                count += seen[need]
            
            seen[prefix_sum] = seen.get(prefix_sum,0) + 1 
    
        return count
            
                
            