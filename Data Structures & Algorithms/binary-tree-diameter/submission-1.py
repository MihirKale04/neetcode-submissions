# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiaDFS(root)
        return self.maxDia
        

    def maxDiaDFS(self, root):
        rightLength = self.maxDepth(root.right)
        leftLength = self.maxDepth(root.left)
        self.maxDia = max(self.maxDia, rightLength + leftLength)
        if root.right:
            self.maxDiaDFS(root.right)
        if root.left:
            self.maxDiaDFS(root.left)
        
        

    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the node is None, the depth is 0
        if root is None:
            return 0

        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The maximum depth is the greater of the two, plus 1 for the current node
        return max(left_depth, right_depth) + 1


        