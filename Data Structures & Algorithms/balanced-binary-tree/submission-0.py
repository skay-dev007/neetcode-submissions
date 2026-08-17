# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.check = True

        def check(root):

            if not root:
                return 0

            left = check(root.left) 
            right = check(root.right) 

            if not (left + 1 == right or left == right or right + 1 == left):
                self.check = False

            return max(left,right) + 1 
        
        check(root)
        return self.check 
            
            


        