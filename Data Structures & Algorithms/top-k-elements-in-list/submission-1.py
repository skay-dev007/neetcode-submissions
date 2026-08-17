class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        for num in nums: 
            counts[num] = counts.get(num,0) + 1 
        
        items = list(counts.items())
        items.sort(key=lambda x:x[1],reverse=True) 

        res = [] 

        for num, cnt in items: 
            if len(res) < k: 
                res.append(num)
            
            else: 
                break 
        
        return res 

 




        