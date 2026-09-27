class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Lets try and simplify this problem to be 
        whether we can figure out if a continous
        group of Os is surrounded or not
        

        we can run dfs on Os and determine that it is surrounded 
        if we reach a border 
            - scan Matrix
            - if O run dfs (up down right left)
            - mark Os as visited
            - if X do nothing
            - if unvisited O continue processing
            - if border return Flase
            - if no border seen then we know that cluster of 0s is surrounded
        """
        
        rowLen, colLen = len(board), len(board[0])
        
        def isSurrounded(r, c) -> bool:
        #determines if O cluster is surrounded
            nonlocal rowLen, colLen
            surrounded = True
            def dfs(r,c, visited):
                nonlocal surrounded
                if r < 0 or c < 0 or r >= rowLen or c >= colLen:
                    surrounded = False
                    return
                if board[r][c] == "X":
                    return
                if (r,c) in visited:
                    return
                visited.add((r, c))
                #up
                dfs(r - 1, c, visited)
                #down
                dfs(r + 1, c, visited)
                #right
                dfs(r, c + 1, visited)
                #left
                dfs(r, c - 1, visited)
            dfs(r,c, set())
            return surrounded
        
        def fill(r, c):  
        #Turns cluster of O to X
            def dfs(r, c):
                if r < 0 or c < 0 or r >= rowLen or c >= colLen:
                    return
                if board[r][c] == "X":
                    return
                board[r][c] = "X"
                #up
                dfs(r - 1, c)
                #down
                dfs(r + 1, c)
                #right
                dfs(r, c + 1)
                #left
                dfs(r, c - 1)
            dfs(r,c)

        
        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c] == "O":
                    if isSurrounded(r, c):
                        print("cluster starting at", r, c, "is surrounded")
                        fill(r, c)
                    else:
                        print("cluster starting at", r, c, "is not surrounded")
        