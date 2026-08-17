# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
 
        
        def construct(root,path):
            if not root:
                path.append("N")
                return 
            
            path.append(str(root.val))
            construct(root.left,path)
            construct(root.right,path)
            return path
        path = construct(root,[]) 
        
        return ",".join(path) if path else ""
  
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.counter = 0 
        if data == "":
            return None
        val = data.split(',')


        def dfs():
            if val[self.counter] == "N":
                self.counter +=1
                return None 

            node = TreeNode(int(val[self.counter]))
            self.counter += 1 
            node.left = dfs()
            node.right = dfs()
            return node 

        return dfs() 
                

            



        

        

        

        

        
