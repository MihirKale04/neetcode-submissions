# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = False
    isValid = True
    found = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def CheckIfValid(root, subRoot):
            if root == None and subRoot == None:
                return
            if root == None or subRoot == None:
                self.isValid = False
                return
            if root.val != subRoot.val:
                self.isValid = False
                return
            CheckIfValid(root.left, subRoot.left)
            CheckIfValid(root.right, subRoot.right)
        def DFS(root):
            if root == None or self.res == True:
                return 
            if root.val == subRoot.val:
                self.found = True
                print("Checking if valid subroot")
                CheckIfValid(root, subRoot)
                if self.isValid == False:
                    self.res = False
                    self.isValid = True
                else:
                    self.res = True
                
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        if self.found:
            return self.res
        return False