from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #right off the bat I know that this is very similar to the 
        #number of islands problem

        #We essentially do the same thing but now when exploring extensions
        #of the island we store the value and update a "max" variable
        
        #lets try to implement using BFS 

        if not grid: #input is empty grid
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set() #This is going to store the visited coordinates
        rows, cols = len(grid), len(grid[0])
        res = 0

        def BFS(r, c):
            area = 0
            q = deque()
            
            area += 1
            visited.add((r,c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    area += 1
                    visited.add((nr, nc))
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = BFS(r, c) #This should return the Area of the island
                    print (currArea)
                    res = max(res, currArea)
        return res
