# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxD = 0
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.maxD
        self.DFS(root, 0)
        return self.maxD
    
    def DFS(self, node: Optional[TreeNode], currDepth: int):
        currDepth += 1
        self.maxD = max(self.maxD, currDepth)
        if node.left:
            self.DFS(node.left, currDepth)
        if node.right:
            self.DFS(node.right, currDepth)
