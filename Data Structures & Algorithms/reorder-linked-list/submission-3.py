# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split linked list into two (first half and second half)
        #reverse the second half of the linked list
        #join the two linked list together
            #use two pointer and iterate accordingly


        #We can get the length of the linkedlist by counting each node 
        length = 0 
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        #to split we need to get two pointers
        #before and after splitting point (halfway)
        if length % 2 == 0:
            splitlen = length //2
        else:
            splitlen = (length // 2) + 1
        before_split = head
        after_split = head
        for i in range(splitlen-1):
            before_split = before_split.next
        for i in range(splitlen):
            after_split = after_split.next

        before_split.next = None
        head2 = after_split

        #Now that we have split the list we need to reverse the second half of the list.
        attachTo = None
        temp = head2
        while temp:
            rev = temp
            temp = temp.next
            rev.next = attachTo
            attachTo = rev
        head2 = attachTo

        #Now we combine the two linkedlists
        first = head
        sec = head2
        for i in range(splitlen):
            if not sec:
                break
            temp = first.next
            temp2 = sec.next
            first.next = sec
            sec.next = temp
            first = temp
            sec = temp2

        return None

