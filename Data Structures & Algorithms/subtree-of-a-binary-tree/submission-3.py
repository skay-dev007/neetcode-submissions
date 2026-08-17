# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(p,q):
            if not p and not q:
                return True 
            if (not p and q) or (p and not q):
                return False 
            
            return p.val == q.val and check(p.left,q.left) and check(p.right,q.right)

        def traverse(root,subRoot):

            if not root:
                return False
            
            if root.val == subRoot.val and check(root,subRoot):
                return True 
            
            return traverse(root.left,subRoot) or traverse(root.right,subRoot) 
        
        return traverse(root,subRoot)



        