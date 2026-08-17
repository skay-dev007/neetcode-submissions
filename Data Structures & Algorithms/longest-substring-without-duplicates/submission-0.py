class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0 
        
        max_len = 0 
        left, right = 0,0
        # alphabet and count ('s':1)
        seen = {}

        while left<= right and right<len(s):

            seen[s[right]] = seen.get(s[right],0) + 1 

            while seen[s[right]] > 1:
                seen[s[left]] = seen.get(s[left]) -1 
                left += 1 

            max_len = max(max_len,(right-left)+1)
            right += 1
        return max_len 


        