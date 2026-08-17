class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_str = "".join([ch.lower() for ch in s if ch.isalnum()])
        return clean_str == clean_str[::-1]

        