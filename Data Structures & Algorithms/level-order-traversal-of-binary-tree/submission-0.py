# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        newLevel = []
        newLevel.append(root)
        res.append([node.val for node in newLevel])
        while True:
            tempLevel = newLevel.copy()
            newLevel = []
            while tempLevel:
                currNode = tempLevel.pop(0)
                if currNode.left:
                    newLevel.append(currNode.left)
                if currNode.right:
                    newLevel.append(currNode.right)
            if newLevel:
                res.append([node.val for node in newLevel])
            else:
                break
        return res