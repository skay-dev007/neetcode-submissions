# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prev = ListNode(0)
        dummy = prev  
        carry = 0 

        
        while l1 and l2:

            val = l1.val + l2.val + carry
            if val <= 9:
                dummy.next = ListNode(val)
                carry = 0 
            else:
                carry = 1
                dummy.next = ListNode(val %10)
            l1 = l1.next
            l2 = l2.next 
            dummy = dummy.next
        
        while l1:
            val = l1.val + carry 
            if val <= 9: 
                dummy.next = ListNode(val)
                carry = 0 
            else: 
                dummy.next = ListNode(val%10)
                carry = 1 

            l1 = l1.next
            dummy = dummy.next 
        
        while l2:
            val = l2.val + carry 
            if val <= 9: 
                dummy.next = ListNode(val)
                carry = 0 
            else: 
                dummy.next = ListNode(val%10)
                carry = 1 

            l2 = l2.next
            dummy = dummy.next 
        
        if carry == 1:
            dummy.next = ListNode(carry)
        
        return prev.next 
        

        
        
            


            

        