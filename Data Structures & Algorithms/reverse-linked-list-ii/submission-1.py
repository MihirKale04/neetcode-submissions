# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prevNode = None
        nextNode = None

        for i in range(right + 1):
            if not nextNode:
                nextNode = head
            else:
                nextNode = nextNode.next
        
        for i in range(left - 1):
            if not prevNode:
                prevNode = head
            else:
                prevNode = prevNode.next

        n = None
        for i in range(left):
            if not n:
                n = head
            else:
                n = n.next

        


        prev = None
        curr = n
        tail = n
        for i in range((right - left)+1):
            print(curr.val)
            temp = curr.next
            curr.next = prev 
            prev = curr
            if i == (right - left):
                break
            curr = temp
        print(curr.val)

        if prevNode:
            prevNode.next = curr
        tail.next = nextNode


        if prevNode:
            return head
        return curr
        


        