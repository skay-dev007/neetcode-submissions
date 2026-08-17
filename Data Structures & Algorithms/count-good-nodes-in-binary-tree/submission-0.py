# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.counter = 0 

        def traverse(node,maxval):

            if not node:
                return 
            
            if node.val >= maxval:
                self.counter += 1 
                print(node.val)
            maxval = max(node.val,maxval) 

            traverse(node.left,maxval)
            traverse(node.right,maxval)
        
        traverse(root,root.val)
        return self.counter 
        