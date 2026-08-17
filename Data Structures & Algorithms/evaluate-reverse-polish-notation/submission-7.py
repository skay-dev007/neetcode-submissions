from collections import deque 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

      stack = deque()

      for token in tokens:
        if token not in {'+','-','/','*'}:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(b+a)
            elif token == '-':
                stack.append(a-b)
            elif token == '/':
                stack.append(int(a/b))
            else:
                stack.append(b*a)
        
      return stack.pop()


