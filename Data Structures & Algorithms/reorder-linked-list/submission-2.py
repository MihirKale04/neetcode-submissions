# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        listcount = 0
        pointer = head

        while pointer != None:
            listcount += 1 
            pointer = pointer.next
        
        if listcount % 2 == 0:
            half = (listcount // 2)
        else:
            half = (listcount // 2) + 1
        
        
        pointer = head
        for i in range(half - 1):
            pointer = pointer.next
        secondhalf = pointer.next
        pointer.next = None
      

        previous = None
        curr = secondhalf
        while (curr):
            nextnode = curr.next
            curr.next = previous
            previous = curr
            curr = nextnode
        
        secondhead = previous

        firsthead = head
        
        while(secondhead):
            firstnext = firsthead.next 
            secondnext = secondhead.next

            firsthead.next = secondhead
            secondhead.next = firstnext

            firsthead = firstnext
            secondhead = secondnext
            

       






