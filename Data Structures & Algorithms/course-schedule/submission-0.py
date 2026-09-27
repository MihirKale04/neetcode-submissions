class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Note: If there is a loop you cannot finish return False
        #Approach:
        #Part1:
            #from input create graph (adjacency matrix)
        adjMatrix = {}
        for prereq in prerequisites:
            adjMatrix[prereq[0]] = adjMatrix.get(prereq[0], [])
            adjMatrix[prereq[1]] = adjMatrix.get(prereq[1], []) 
            adjMatrix[prereq[1]].append(prereq[0])   
        #Part2:
            #find cycle in graph
            #don't know if this is correct but I think its important to start form 
            #each course that has no prerequisites
                #to detect this we 
        def checkCycle(adjList):
            N = len(adjList)
            visited = set()
            in_stack = set()
            def dfs(node):
                visited.add(node)
                in_stack.add(node)
                for neigh in adjList[node]:
                    if neigh not in visited: 
                        if dfs(neigh):
                            return True
                    elif neigh in in_stack:
                        return True
                    
                in_stack.remove(node)
                return False
            
            for node in adjList.keys():
                if node not in visited:
                    if dfs(node):
                        return True
            return False

        
        
        hasCycle = checkCycle(adjMatrix)
        if hasCycle:
            return False
        return True