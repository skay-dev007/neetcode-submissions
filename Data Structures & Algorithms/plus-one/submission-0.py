class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder,carry = 0,1
        results = []

        for digit in digits[::-1]:
            remainder = carry + digit 
            if remainder > 9:
                remainder %= 10 
                carry = 1 
            else:
                carry = 0 
            results.append(remainder)
        if carry == 1:
            results.append(1)
        return results[::-1]

        