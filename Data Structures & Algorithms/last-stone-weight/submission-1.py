import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [ -stone for stone in stones]
        heapq.heapify(heap)
        

        while len(heap) > 1:

            x = heapq.heappop(heap) * -1 
            y = heapq.heappop(heap) * -1 

            if x != y:
                diff = abs(x - y)
                heapq.heappush(heap, -diff)
            
        return -heap[0] if len(heap) == 1 else 0 

            
        