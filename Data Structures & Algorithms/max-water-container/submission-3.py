class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) -1 
        max_water = 0 

        while left<right:

            h = min(heights[right],heights[left]) 
            w= right-left 

            water = h * w 
            if water > max_water:
                max_water = water 
            
            if heights[left] < heights[right]: 
                left += 1 
            else:
                right -=1 

        return max_water 

