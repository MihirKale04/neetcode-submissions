from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #We can implement a BFS
        # When we add to queue we append the last node in queue to res 
        # for each level
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        newq = deque()
        res.append(root.val)
        while True:
            while q:
                node = q.popleft()
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
            if not newq:
                break
            res.append(newq[-1].val)
            q = newq
            newq = deque()
        return res
