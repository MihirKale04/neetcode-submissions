# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def DFS(node, l, r):
            nonlocal res
            if not node:
                return
            print(l,node.val, r)

            if not (node.val < r and node.val > l):
                res = False
                return 
            
            DFS(node.left,l,node.val)
            DFS(node.right, node.val, r)
        DFS(root,float('-inf'), float('inf'))
        return res
            