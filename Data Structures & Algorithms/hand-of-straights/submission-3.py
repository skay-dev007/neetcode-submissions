from collections import Counter 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counts = dict(Counter(hand))
        hand.sort()

        for num in hand:
            if counts[num]:
                for item in range(num, num+groupSize):
                    if counts.get(item,-1) <= 0:
                        return False 
                    
                    counts[item] -= 1 
        
        return True 
        
        
         
           












        
        