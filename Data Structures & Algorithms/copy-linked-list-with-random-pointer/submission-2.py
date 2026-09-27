"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        objMap = {} #old -> new 
        #first pass: create the new nodes and init objMap
        curr = head
        while curr:
            newNode = Node(curr.val)
            objMap[curr] = newNode
            curr = curr.next

        #second pass: we might be able to link both the next and the random nodes
        #to the appropriate nodes
        curr = head
        while curr:
            copy = objMap[curr]
            if curr.next:
                copy.next = objMap[curr.next]
            else:
                copy.next = None
            if curr.random:
                copy.random = objMap[curr.random]
            else:
                copy.random = None
            curr = curr.next  

        return objMap[head]  
        