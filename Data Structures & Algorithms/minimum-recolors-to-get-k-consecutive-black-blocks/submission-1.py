class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_w = len(blocks)
        curr_w = 0 


        for i,char in enumerate(list(blocks)):
            if char == 'W':
                curr_w += 1 

            if i>=k:
                if blocks[i-k] == 'W':
                    curr_w -= 1 
            
            if i>= k-1 and min_w > curr_w:
                min_w = curr_w 
            
        
        return min_w 

            
            


        