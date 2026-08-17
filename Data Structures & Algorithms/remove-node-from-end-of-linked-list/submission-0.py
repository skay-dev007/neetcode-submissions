# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        #legnth of list 
        length = 0 
        curr = head 
        while curr:
            length += 1 
            curr = curr.next 
        
        dist_from_front = length - n 
        counter = 0 
        prev = None 
        curr = head 

        if dist_from_front == 0:
            return head.next

        while counter < dist_from_front:
            prev = curr
            curr = curr.next 
            counter += 1 

        prev.next = curr.next

        return head 
        



        