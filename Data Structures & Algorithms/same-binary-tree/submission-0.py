# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(first,second):
            if not first and not second:
                return True 
            if (not first and second) or (not second and first):
                return False  

            return (first.val == second.val) and traverse(first.left,second.left) and traverse(first.right,second.right) 

        return traverse(p,q)
        