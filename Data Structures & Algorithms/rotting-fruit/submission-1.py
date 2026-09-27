from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #We initialize by finding the rotten oranges and storing them in a queue
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        #We run BFS looking for neighboring fresh fruit
        minutes = 0
        while rotten:
            n = len(rotten)
            foundRotten = False
            for i in range(n):
                currRow, currCol = rotten.popleft()
                #up
                if currRow - 1 >= 0:
                    if grid[currRow - 1][currCol] == 1:
                        grid[currRow - 1][currCol] = 2
                        rotten.append((currRow - 1, currCol))
                        foundRotten = True

                #down
                if currRow + 1 < rows:
                    if grid[currRow + 1][currCol] == 1:
                        grid[currRow + 1][currCol] = 2
                        rotten.append((currRow + 1, currCol))
                        foundRotten = True

                #right
                if currCol + 1 < cols:
                    if grid[currRow][currCol + 1] == 1:
                        grid[currRow][currCol + 1] = 2
                        rotten.append((currRow, currCol + 1))
                        foundRotten = True

                #left
                if currCol - 1 >= 0:
                    if grid[currRow][currCol - 1] == 1:
                        grid[currRow][currCol - 1] = 2
                        rotten.append((currRow, currCol - 1))
                        foundRotten = True
                
            #if we found a rotten fruit inc minute
            if foundRotten:
                minutes += 1
        
        #We could do a final scan of the grid searching for fresh fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes

        