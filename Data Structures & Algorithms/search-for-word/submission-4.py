class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        res = False
        
        def peepBoard(cord , wordIdx):
            nonlocal res
            r, c = cord

            if r < 0 or r >= rows or c < 0 or c >= cols: #bounds check
                # print("out of bounds")
                return
            
            #check if letter is valid
            if not board[r][c] == word[wordIdx]:
                # print("not valid")
                return

            if wordIdx == len(word) - 1: #We have reached the end so we found the word
                res = True
                return   
            
            
             
            


            visited.add((r,c))

            print(board[r][c], r, c)
            #down
            if not (r + 1, c) in visited:
                # print("going down")
                peepBoard((r+1, c), wordIdx + 1)
            #up
            if not (r - 1, c) in visited:
                # print("going up")
                peepBoard((r - 1, c), wordIdx + 1)
            #left
            if not (r, c - 1) in visited:
                # print("going left")
                peepBoard((r , c - 1), wordIdx + 1)
            #right
            if not (r, c + 1) in visited:
                # print("going right")
                peepBoard((r, c + 1), wordIdx + 1)


            visited.discard((r,c))
           
        
        wordIdx = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[wordIdx]: #find start
                    visited.clear()
                    # print("starting at:", r, c )
                    peepBoard((r,c), wordIdx)

        return res
