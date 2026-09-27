class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #We can create another grid but it will store
        #visited/not-visited

        #When we approach a 1 we can try to do a DFS (up down right left)
        #for every "1" we visit in the DFS we can check if it has been visited

        #If we find a 1 that has not been visited we know that it is an island





        yLen = len(grid)
        xLen = len(grid[0])
        visited = [[False for _ in range(xLen)] for _ in range(yLen)]
        res = 0


        """This func runs through grid with a start point and does DFS in all 
        for directions looking for ones updating visited"""
        def multiDirectionalDFS(x, y):
            #bounds checks
            if x < 0 or x >= xLen:
                return

            if y < 0 or y >= yLen:
                return

            if grid[y][x] == "0":
                return

            #found extenstion of island
            if grid[y][x] == "1" and not visited[y][x]:
                visited[y][x] = True
                multiDirectionalDFS(x + 1, y)
                multiDirectionalDFS(x, y + 1)
                multiDirectionalDFS(x - 1, y)
                multiDirectionalDFS(x, y - 1)

        for y in range(yLen):
            for x in range(xLen):
                if grid[y][x] == "1" and not visited[y][x]:
                    res += 1
                    multiDirectionalDFS(x, y)
    
                   
        return res


        