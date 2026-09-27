class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #High Level Approach
        #If there is a cycle than graph is not a valid tree

        #Step 1:
        #Create AdjList
        def createAdjList(edges):
            adjList = {i: [] for i in range(n)}
            for source, dest in edges:
                adjList[source] = adjList.get(source, [])
                adjList[dest] = adjList.get(dest, [])
                adjList[source].append(dest)
                adjList[dest].append(source)
            return adjList
        adjList = createAdjList(edges)


        #Step 2:
        #run dfs on every unvisited node to detect for cycle
        def hasCycle(adjList):
            visited = set()
            def dfs(node, parent):
                if node in visited:
                    return True
                visited.add(node)
                for neigh in adjList[node]:
                    if neigh == parent:
                        continue
                    if dfs(neigh, node):
                        return True
                return False

        
            if dfs(0, -1) or len(visited) != n:
                return True
            return False
           


        if hasCycle(adjList):
            return False
        return True