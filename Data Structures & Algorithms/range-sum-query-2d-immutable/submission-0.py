class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sumMatrix = self.generateSumMatrix(self.matrix)


    def generateSumMatrix(self, matrix:  List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        newMatrix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        
        #first past just the cols 
        for r in range(rows):
            for c in range(cols):
                newMatrix[r + 1][c + 1] = matrix[r][c] + newMatrix[r + 1][c]
            
    
        #second pass just the rows 
        for r in range(rows):
            for c in range(cols):
                newMatrix[r + 1][c + 1] = newMatrix[r + 1][c + 1] + newMatrix[r][c + 1]
        return newMatrix



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        subLeft = (row2 + 1, col1)
        subTop = (row1, col2 + 1)
        addTopLeft = (row1, col1)
        addFull = (row2 + 1, col2 + 1)
        res = 0

        res += self.sumMatrix[addFull[0]][addFull[1]]


        res += self.sumMatrix[addTopLeft[0]][addTopLeft[1]]

        res -= self.sumMatrix[subLeft[0]][subLeft[1]]
        res -= self.sumMatrix[subTop[0]][subTop[1]]
        
        
        return  res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)





"""

2 3 1 3
2 1 3 2
4 2 1 3 

sumRegion((0, 0), (1, 1)) -> 8
sumRegion((0, 1), (3, 4)) -> 6 + 5 + 8 = 19 

"""