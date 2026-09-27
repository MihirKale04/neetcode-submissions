# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        def DFS(root: Optional[TreeNode]) -> None:
            if not root:
                return
            print (getDepth(root.left, 0), getDepth(root.right, 0))
            if abs(getDepth(root.left, 0) - getDepth(root.right, 0)) > 1:
                self.res = False
            DFS(root.left)
            DFS(root.right)

            
        def getDepth(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth
            return max(getDepth(root.right, depth + 1), getDepth(root.left, depth + 1))
            
        DFS(root)
        return self.res
       









    
 
             



        


        