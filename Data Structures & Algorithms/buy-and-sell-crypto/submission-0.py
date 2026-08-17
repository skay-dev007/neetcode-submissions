class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val, ptr = prices[0],0
        max_val = 0 

        while ptr < len(prices):
            if ptr > 0:
                min_val = min(min_val,prices[ptr-1])
            
            sell = prices[ptr]
            max_val = max(max_val,sell - min_val)
            ptr += 1

        return max(max_val,0)

            



        