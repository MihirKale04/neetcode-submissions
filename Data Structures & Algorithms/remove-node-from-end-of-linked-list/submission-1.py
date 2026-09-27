# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #figure out the length of the list (by traversal)
        #subtract length by n to figure out the node that needs to be deleted
        #have a pointer that always points to the head (to return)
        #have a pointer that traverses to len - n (to adjust the next pointer to skip the deleted node)
        #have another pointer traverse to the deleted node (so that its next pointer is set to null)
        
        #initialize our pointers
        # prev = ListNode(None)
        # prev.next = head
        res = head
        p1 = head #this will be used to adjust the linkedlist to skip over the deleted node
        p2 = head #this will be used to make sure the deleted node next is null
        length = 0
        while head:
            length += 1
            head = head.next
        
        if not length - n  > 0:
            res = res.next
            return res

        #set p1 and p2 to the appropriate spots 
        for i in range(length-n-1):
            p1 = p1.next
        
        for i in range(length-n):
            p2 = p2.next
        print("length and n:",length, n)
        print(p1.val, p2.val)
        p1.next = p2.next
        p2.next = None
        return res