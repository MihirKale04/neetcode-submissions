"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        #Init mapping
        mapping = {}
        toVisit = []
        while True:
            mapping[node.val] = node.neighbors
            for n in node.neighbors:
                if n.val not in mapping:
                    toVisit.append(n)
            if not toVisit:
                break
            node = toVisit.pop()
        
        #Use mapping to create copy
        nodeArr = []   
        nodeArr = [None for _ in range(len(mapping))]
        for key in mapping: #Init node array with vals
            newNode = Node()
            newNode.val = key
            nodeArr[key - 1] = newNode
        
        for key in mapping: #Link neighbors accordingly
            node = nodeArr[key - 1]
            for n in mapping[key]:
                node.neighbors.append(nodeArr[n.val - 1])
            
        return nodeArr[0]
        