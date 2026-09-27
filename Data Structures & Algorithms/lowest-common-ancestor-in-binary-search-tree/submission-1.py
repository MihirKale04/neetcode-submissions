# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #First lets just see if we can detect p and q

        

        pset = set()
        #lets first find p
        curr = root
        res = curr # init result to be the root
        while True: 
            if curr == None:
                break
            
            if curr.val == p.val:
                pset.add(curr)
                break

            pset.add(curr)
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right



        # shared = set()
        #lets first find q
        curr = root
        while True: 
            if curr == None:
                break
            
            if curr.val == q.val:
                if curr in pset:
                    res = curr
                break
            
            if curr in pset:
                res = curr
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right



        return res
