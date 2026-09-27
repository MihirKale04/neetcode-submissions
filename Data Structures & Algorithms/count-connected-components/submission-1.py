class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def createAdjList(edges):
            adjList = {i:[] for i in range(n)}
            for source, dest in edges:
                adjList[source].append(dest)
                adjList[dest].append(source)
            return adjList
        
        
        #from edges make an adjList 
        adjList = createAdjList(edges)
    

        #run dfs on unvisited node 
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in adjList[node]:
                dfs(neigh)
            return 

        
        count = 0 
        for node in adjList:
            if node not in visited:
                dfs(node)
                count +=1
        #return the count of dfs's we ran
        return count