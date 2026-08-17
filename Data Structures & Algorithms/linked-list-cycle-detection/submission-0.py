# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return False 

        first, second = head, head

        while first and second: 
            first = first.next 
            second = second.next.next 

            if first == second:
                return True 

        return False 

        