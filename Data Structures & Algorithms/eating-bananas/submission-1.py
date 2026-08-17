class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def checkValid(k):
            total_time = 0 
            for pile in piles:
                total_time += math.ceil(pile/k)
            return total_time 

        # we have to search for k 
        # a valid K is when it sums to a time of <= h 

        low,high = 1,max(piles) 
        

        while low< high:

            k = low + ((high-low)//2)

            get_k_time = checkValid(k)

            if get_k_time <= h:
                high = k  
            else:
                low = k+1 

        return low  


        