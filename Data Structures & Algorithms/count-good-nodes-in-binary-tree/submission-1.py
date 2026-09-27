import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        maxValPath = -sys.maxsize - 1
        def DFS(node, maxValPath):
            nonlocal res
            if not node:
                return
            good = True
            print(node.val,maxValPath)
            if node.val >= maxValPath:
                maxValPath = node.val
                res += 1
            DFS(node.left, maxValPath)
            DFS(node.right, maxValPath)
        DFS(root, maxValPath)
        return res

