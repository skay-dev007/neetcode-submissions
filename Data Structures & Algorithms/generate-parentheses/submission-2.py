class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []
        
        results = []
        def gen(nOpen,nClosed,current):

            if nOpen == nClosed == n: 
                results.append("".join(current))
                return 
            
            if nClosed < nOpen:
                current.append(")")
                gen(nOpen,nClosed+1,current)
                current.pop()

            if nOpen < n:
                current.append("(")
                gen(nOpen+1,nClosed,current)
                current.pop()
        
        gen(0,0,[])
        return results
