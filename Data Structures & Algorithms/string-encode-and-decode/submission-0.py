class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        res = ""
        for string in strs:
            res += str(len(string)) + ',' + string 

        return res


    def decode(self, s: str) -> List[str]:

        result = []
        start_idx = 0
        end_idx = 0

        print(s)
        while end_idx < len(s):
            if s[end_idx] != ',':
                end_idx += 1 
                continue 
            else:
                length = int(s[start_idx:end_idx])
                word = s[end_idx+1:end_idx+1 +length]
                result.append(word)
                end_idx = end_idx + length + 1 
                start_idx = end_idx
        
        return result 




            
            

