class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #what we can do is perform dfs starting from the borders for both pacific and atlantic
        rowLen, colLen = len(heights), len(heights[0])
        pac, atl = set(), set() 
        def dfs(r, c, ocean, prevHeight):
            if (r, c) in ocean:
                return
            if r < 0 or c < 0 or r >= rowLen or c >= colLen:
                return
            if heights[r][c] < prevHeight:
                return
            
            ocean.add((r, c))
            #up
            dfs(r - 1, c, ocean, heights[r][c])
            #down
            dfs(r + 1, c, ocean, heights[r][c])
            #left 
            dfs(r , c - 1, ocean, heights[r][c])
            #right
            dfs(r, c + 1, ocean, heights[r][c])


        for col in range(colLen):
            dfs(0, col, pac, 0)
            dfs(rowLen - 1, col, atl, 0)
        
        for row in range(rowLen):
            dfs(row, 0, pac, 0)
            dfs(row, colLen - 1, atl, 0)
        
        cells = []
        
        #The result will be a union of both those sets
        #get the union of pac and atl
        for r in range(rowLen):
            for c in range(colLen):
                if (r, c) in pac and (r, c) in atl:
                    cells.append([r, c])
        return cells


        