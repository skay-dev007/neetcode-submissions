class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for index in range(len(strs[0])):
            for string in strs: 
                if len(string) == index or strs[0][index] != string[index]:
                    return strs[0][:index] 
            
        return strs[0]

            
        
        