from collections import Counter, defaultdict 
class Solution:
    def gethash(self,string):
        res = [0]*26 
        base = ord('a')
        for ch in string:
            res[ord(ch)-base] += 1 
        return res 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = defaultdict(list)

        for string in strs:
            hash_ = self.gethash(string)
            results[tuple(hash_)].append(string)
        
        return list(results.values())


        

        
                


        
        