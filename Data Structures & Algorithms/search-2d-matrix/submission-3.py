class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def calcMiddle(Start: int, End: int) -> int:
            if (((End-Start) + 1) % 2 == 0):
                Middle = ((Start + End) // 2) + 1
            else:
                Middle = ((Start + End) // 2) 
            return Middle  

        res = False
        
        rowsNum = len(matrix)
        columnNum = len(matrix[0])
        rowStart = 0
        rowEnd = rowsNum - 1 
        rowMiddle = calcMiddle(rowStart, rowEnd)
        while rowStart != rowEnd: 
            print (rowStart, rowEnd, rowMiddle)
            if target > matrix[rowMiddle][0]:
                rowStart = rowMiddle
                rowMiddle = calcMiddle(rowStart, rowEnd)           
            elif target < matrix[rowMiddle][0]:
                rowEnd = rowMiddle - 1   
                rowMiddle = calcMiddle(rowStart, rowEnd)
            else:
                return True
            
        targetRow = matrix[rowMiddle]
        print (targetRow)

        colStart = 0
        colEnd = columnNum - 1
        colMiddle = calcMiddle(colStart, colEnd)
        while colStart!=colEnd:
            if target > targetRow[colMiddle]:
                colStart = colMiddle
                colMiddle = calcMiddle(colStart, colEnd)
            elif target < targetRow[colMiddle]:
                colEnd = colMiddle - 1
                colMiddle = calcMiddle(colStart, colEnd)
            else:
                return True
      
        if targetRow[colMiddle] == target:
            return True
        if (rowsNum == 1 and columnNum == 1):
            if target == matrix[0][0]:
                return True


        return False


