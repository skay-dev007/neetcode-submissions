class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 
        max_len = 0
        store = {}

        for right in range(len(s)):

            store[s[right]] = store.get(s[right],0) + 1

            curr_max = max(store.values())

            #valid window window_size - max_item <= k 
            while ((right - left + 1) - curr_max )> k:
                store[s[left]] -= 1
                left += 1 
            
            max_len = max(max_len,right - left + 1)
        
        return max_len







        