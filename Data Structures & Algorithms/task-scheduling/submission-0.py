from collections import deque, Counter  
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #create a max heap 
        # keep addidng to queue, and removing from queue when that time is reached 
        # when poped from queue if count > 0 re add it to max heap 
        # we want them in max order as they would take the most time 

        counts = Counter(tasks)
        maxHeap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while queue or maxHeap:

            time += 1 
            if maxHeap:
                curr = 1 + heapq.heappop(maxHeap)
                if curr < 0:
                    queue.append((time + n,curr))

            while queue and queue[0][0] <= time:
                _, curr = queue.popleft()
                if curr<0:
                    heapq.heappush(maxHeap, curr)
            
        
        return time
                




        