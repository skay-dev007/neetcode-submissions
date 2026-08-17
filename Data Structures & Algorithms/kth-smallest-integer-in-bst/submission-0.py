# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        def traverse(root,path):
            if not root:
                return 
    
            traverse(root.left,path)
            path.append(root.val) 
            traverse(root.right,path)

            return path 
    
              
        path = traverse(root,[])
        return path[k - 1]




        