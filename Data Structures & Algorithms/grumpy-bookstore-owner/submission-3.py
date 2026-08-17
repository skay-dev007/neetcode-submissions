class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curr_satisfied = 0 

        for i in range(len(customers)):
            if grumpy[i] == 0: 
                curr_satisfied += customers[i] 
     
        max_range = 0 
        curr_max = 0 

        for i in range(len(customers)): 
            if grumpy[i] == 1:
                curr_max += customers[i]

            if i>= minutes and grumpy[i-minutes] == 1:
                curr_max -= customers[i-minutes] 
            if i>= minutes -1  and max_range < curr_max:
                max_range = curr_max 
        
        return curr_satisfied + max_range

            
            
            

                
        