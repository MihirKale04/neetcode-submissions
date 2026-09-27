class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        #iterate through each 3 * 3 square
        #check for duplicates
            #if interger is 1-9 add to set
            #if we find an interger that is already in the set return false
        #if we go through each 3 * 3 without finding any duplicates in each then return true
        
        
        #I am going to assume that the input board has lengths that's divisible by 3
        def gridValid(r, c):
            nums = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] in "123456789":
                        if board[i][j] in nums:
                            return False
                        nums.add(board[i][j])
            return True
        
        def rowValid(r):
            nums = set()
            for c in range(cols):
                if board[r][c] in "123456789":
                        if board[r][c] in nums:
                            return False
                        nums.add(board[r][c])
            return True


        def colValid(c):
            nums = set()
            for r in range(rows):
                if board[r][c] in "123456789":
                        if board[r][c] in nums:
                            return False
                        nums.add(board[r][c])
            return True
        
        
        #check if each 3 * 3 grid is valid
        for r in range(0, rows, 3):
            for c in range(0, cols, 3):
                if not gridValid(r, c): #we pass in the starting index
                    return False

        #check if each row is valid
        for r in range(rows):
            if not rowValid(r):
                return False

        #check if each col is valid
        for c in range(cols):
            if not colValid(c):
                return False

        return True