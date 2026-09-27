from copy import deepcopy
from collections import defaultdict
from collections import deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #From the tickets array we need to constuct a graph
            #We can potentially do an adjacency matrix
        adjMatrix = defaultdict(list)
        for source, dest in tickets:
            adjMatrix[source].append(dest) 
        #sort each dest in descending order
        for source in adjMatrix:
            adjMatrix[source].sort(reverse=True)
        print(adjMatrix)
        #We run EulerianPath DFS on our graph (adjency matrix)
        path = deque()
        def DFS(source):
            while(adjMatrix[source]):
                nextDest = adjMatrix[source].pop()
                DFS(nextDest)
            path.appendleft(source)      
        DFS('JFK')

        return list(path)

        

