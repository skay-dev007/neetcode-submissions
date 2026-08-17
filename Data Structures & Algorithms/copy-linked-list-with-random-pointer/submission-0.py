"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # first list to copy 
        mappings = {}

        curr = head 
        dummy = Node(0) 
        new_ptr = dummy 

        while curr:

            new_ptr.next = Node(curr.val)
            new_ptr = new_ptr.next 

            mappings[curr] = new_ptr 
            curr = curr.next 

        curr = head
        new_ptr = dummy.next  

        while curr: 
            if curr.next:
                new_ptr.next = mappings[curr.next]
            else:
                new_ptr.next = None 

            if curr.random: 
                new_ptr.random = mappings[curr.random]
            else:
                new_ptr.random = None 
            curr = curr.next 
            new_ptr = new_ptr.next 
        
     
        return dummy.next 






        