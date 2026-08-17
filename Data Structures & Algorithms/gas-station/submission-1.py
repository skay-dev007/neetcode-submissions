class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = len(gas)
        done = None  
        for start in range(total):
            curr_total = 0
            completed = True 
            for next_index in range(total):
                i = (start + next_index) % total 
                curr_total += gas[i] - cost[i]
                if curr_total < 0:
                    completed = False 
                    break 
            if completed:
                return start  
    
        return -1           
            









