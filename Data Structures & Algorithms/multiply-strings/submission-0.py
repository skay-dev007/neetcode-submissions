class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        inum1, inum2 = 0,0 
        for index in range(len(num1)):
            inum1 += (int(num1[len(num1)-1 -index]) * 10**index) 
        
        for index in range(len(num2)):
            inum2 += (int(num2[len(num2)-1-index])* 10**index)
        
        return str(inum1*inum2)




        