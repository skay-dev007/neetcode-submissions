# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        currmax = 0 
        def traverse(root):
            nonlocal currmax
            if not root:
                return 0 
            
            left = traverse(root.left)
            right = traverse(root.right)

            currmax = max(currmax, left + right)
            return max(left, right) + 1 
        traverse(root)
        return currmax 
            
            




            
            
            

            







        