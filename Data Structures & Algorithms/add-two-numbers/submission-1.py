# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode()
        head = prev
        while l1 or l2:
            if not l1:
                newVal = l2.val + carry
            elif not l2:
                newVal = l1.val + carry
            else:
                newVal = l2.val + l1.val + carry
            if newVal >= 10:
                newVal = newVal % 10
                carry = 1
            else: 
                carry = 0 
            #create and add newNode
            newNode = ListNode(newVal)
            prev.next = newNode
            prev = prev.next
            #shift l1 and l2 pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #add a carried 1 at the end if applicapble 
        if carry:
            prev.next = ListNode(1)
        return head.next