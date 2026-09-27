# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        while head:
            visited[head.val] = visited.get(head.val, 0) + 1
            if visited[head.val] > 1:
                return True
            print(visited)
            head = head.next
        return False
        