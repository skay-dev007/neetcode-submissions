class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[pos,s] for pos,s in zip(position,speed)]

        stack = []
        for pos,s in sorted(pairs)[::-1]:
            time = (target-pos)/s
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)


        
        