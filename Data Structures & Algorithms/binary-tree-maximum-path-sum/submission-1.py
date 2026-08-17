# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:



        self.maxval = root.val if root.val else 0 
        def traverse(root):

            if not root:
                return -1001  
            
            if not root.left and not root.right:
                return root.val 
            
            left = traverse(root.left)
            right = traverse(root.right)

            self.maxval = max(left,right,left+root.val,root.val+right,root.val+left+right,self.maxval,)

            return max(left+root.val,right+root.val,root.val)

        traverse(root)
        return self.maxval 

        