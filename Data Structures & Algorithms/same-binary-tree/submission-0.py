# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array1 = []
        array2 = []
        def DFS(root: Optional[TreeNode], array: []):
            if not root:
                array.append(None)
                return
            array.append(root.val)
            DFS(root.left, array)
            DFS(root.right, array)
        DFS(p, array1)
        DFS(q, array2)
        if (array1 == array2):
            return True
        return False 




        