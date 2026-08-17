# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy 
        k = len(lists)

        while any(lists):
            #refresh the loop
            min_index = None 

            for index in range(k):
                if lists[index]:
                    ptr = lists[index]
                    if min_index != None and ptr.val < lists[min_index].val: 
                        min_index = index 
                    elif min_index == None:
                        min_index = index 
        
            curr.next = lists[min_index] 
            curr = curr.next 
            lists[min_index] = lists[min_index].next
        
        curr.next = None
        return dummy.next  



              
            







        