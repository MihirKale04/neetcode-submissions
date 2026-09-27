# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we could simply do DFS each time we reach/process a node we return a count
        #when count == k we store that value somewhere and return it
        count = 0
        res = 0
        def dfs(node):
            nonlocal res
            nonlocal count
            if not node:
                return
            dfs(node.left)
            
            count += 1
            print(count, node.val)
            if count == k:
                res = node.val
            dfs(node.right)
        dfs(root)
        return res

    
        