class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        curr = None 
        for triplet in triplets:
            a,b,c = triplet 
    
            if a <= target[0] and b<= target[1] and c<= target[2]:
                if curr:
                    curr = [max(a,curr[0]), max(b,curr[1]), max(c,curr[2])]
                else:
                    curr = triplet 
            
        return True if curr == target else False 
          

            


        