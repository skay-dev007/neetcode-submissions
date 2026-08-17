# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque()
        curr = root
        queue.append(root)

        while queue:

            curr_len = len(queue)
            for nodes in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                left = node.left 
                right = node.right 

                node.left = right 
                node.right = left 

        return root
            
             


        