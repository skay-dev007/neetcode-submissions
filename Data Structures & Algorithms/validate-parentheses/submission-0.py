class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for token in s:
            if token in ['(','[','{']:
                stack.append(token)
            elif token == ')':
                if not stack or stack[-1] != '(':
                    return False 
                else:
                    stack.pop()
            elif token == ']':
                if not stack or stack[-1] != '[':
                    return False 
                else:
                    stack.pop()
            
            else:
                if not stack or stack[-1] != '{':
                    return False 
                else:
                    stack.pop()
        
        return True if not stack else False 







        