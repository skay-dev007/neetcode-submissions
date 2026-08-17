class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[pos,s] for pos,s in zip(position,speed)]
        pairs = sorted(pairs,key = lambda x:x[0])
        stack = []

        for pos,s in pairs[::-1]:
            time = (target-pos) /s 
            if stack:
                if time > stack[-1]:
                    stack.append(time) 
            else:
                stack.append(time)
    
        return len(stack)
            






        