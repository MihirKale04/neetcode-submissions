from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def BFS(row, col): 
            q = deque()
            level = 0
            q.append((row, col, level))
            while q:
                row, col, level = q.pop()
                if level < grid[row][col]:
                    grid[row][col] = level
                #up
                if row - 1 >= 0 and grid[row - 1][col] > level + 1:
                    q.append((row - 1, col, level + 1))
                #down
                if row + 1 < len(grid)  and grid[row + 1][col] > level + 1:
                    q.append((row + 1, col, level + 1))
                #right 
                if col + 1 < len(grid[0]) and grid[row][col + 1] > level + 1:
                    q.append((row, col + 1, level + 1))
                #left
                if col - 1 >= 0 and grid[row][col - 1] > level + 1:
                    q.append((row, col - 1, level + 1))
        
        #locate the treasure
        rlen = len(grid)
        clen = len(grid[0])
        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 0:
                    print("found tresure!! at:", r, c)
                    BFS(r, c) #Run BFS starting from the treasure  
        


