class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def common(word1,word2):
            w1, w2 = len(word1), len(word2)
            end = min(w1,w2)
            start = 0 

            if end == 0: 
                return ""

            while start<end:
                if word1[start] == word2[start]:
                    start += 1 
                else: 
                    return word1[:start] 

            return word1[:end] 
        
        total_words = len(strs) 
        if total_words == 1:
            return strs[0]
        
        common_word = strs[0]
        words_n = 1 
        while words_n < total_words:
            common_word = common(common_word,strs[words_n])
            if common_word == "":
                return ""
            words_n += 1  
        
        return common_word




         
        