"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node 

        neighbors = deque() 
        mapping = {node:Node(node.val)}
        neighbors.append(node)

        while neighbors:
            curr_node = neighbors.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    neighbors.append(neighbor)
                mapping[curr_node].neighbors.append(mapping[neighbor])
                
        return mapping[node]
            
                


                     



        

        

        

         
        