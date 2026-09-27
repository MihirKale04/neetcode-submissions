# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        parents = []
        
        def DFS(node):
            if not node:
                return
            nonlocal res
            good = True
            print(parents)
            for val in parents:
                if val > node.val:
                    #not good we dont inc the res
                    good = False
            if good:
                res += 1
            
            parents.append(node.val)
            DFS(node.left)
            DFS(node.right)
            parents.pop()
    

        DFS(root)

        return res