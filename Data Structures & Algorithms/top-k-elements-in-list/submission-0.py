import heapq 
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for element in nums:
            freq_dict[element] = freq_dict.get(element,0) + 1 
        
        #create an array with (-freq,ele)
        #because python has heapq as min heap be default and we want to make it a max heap 

        heap = [(-freq,element) for (element,freq) in freq_dict.items()]
        heapq.heapify(heap)
        
        result = []
        while k>0:
            freq,ele = heapq.heappop(heap)
            result.append(ele)
            k-= 1 
        return result 





        