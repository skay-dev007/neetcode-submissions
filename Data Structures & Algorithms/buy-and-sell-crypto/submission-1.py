class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        min_val = prices[0]

        for index in range(len(prices)):
            profit = prices[index] - min_val 
            max_profit = max(profit,max_profit) 
            min_val = min(min_val,prices[index]) 


        return max(max_profit,0)


        

            



        