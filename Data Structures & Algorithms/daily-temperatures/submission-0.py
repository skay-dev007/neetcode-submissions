from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = deque()
        results = [0]*len(temperatures)
        for ele_index in range(len(temperatures)):

            while stack and stack[-1][0]<temperatures[ele_index]:
                _,top_index = stack.pop()
                results[top_index] = ele_index - top_index 
                
            stack.append((temperatures[ele_index],ele_index))
            
        return results


            
        