from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def create_code(string):
            code = [0]*26
            for char in string:
                code[ord(char)-ord('a')] += 1 
            return tuple(code) 
        
        store = defaultdict(list) 
        for string in strs: 
            hash_ = create_code(string)
            store[hash_].append(string)
        
        return list(store.values())




        