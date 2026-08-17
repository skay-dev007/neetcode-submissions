class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0 
        
        store = {}
        left,right = 0,0 
        max_len = 0 

        while left<= right and right<len(s):

            store[s[right]] = store.get(s[right],0) + 1

            if store[s[right]] > 1:
                while store[s[right]] > 1:
                    store[s[left]] = store.get(s[left]) -1 
                    left += 1
            
            max_len = max(max_len,right-left+1)
            right +=1 
        
        return max_len