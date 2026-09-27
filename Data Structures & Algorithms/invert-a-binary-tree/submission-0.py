# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node = root
        if node:
            self.invertNode(node)
        return root

    def invertNode(self, node: Optional[TreeNode]):
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left:
            self.invertNode(node.left)
        if node.right:
            self.invertNode(node.right)