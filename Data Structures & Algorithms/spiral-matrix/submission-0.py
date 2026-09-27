class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        r,c = 0, 0

        #init start
        res.append(matrix[r][c])
        visited.add((r,c))

        while True:
            updated = False
            #Go as far right as possible
            while True:
                #check if I can increment first
                if (r, c + 1) in visited or c + 1 >= len(matrix[0]):
                    break 
                c += 1 # move right
                updated = True
                res.append(matrix[r][c])
                visited.add((r,c))
            print(visited)
            print(res)

            # go as far down
            while True:
                #bounds check
                if (r + 1,c) in visited or r + 1 >= len(matrix):
                    break 
                r += 1
                updated = True
                res.append(matrix[r][c])
                visited.add((r,c))
            print(visited)
            print(res)


            # go as far left
            while True:
                #bounds check
                if (r ,c - 1) in visited or c - 1 <  0:
                    break 
                c -= 1
                updated = True
                res.append(matrix[r][c])
                visited.add((r,c))
            print(visited)
            print(res)

            # go as far up
            while True:
                #bounds check
                if (r - 1, c) in visited or r - 1  < 0:
                    break 
                r -= 1
                updated = True
                res.append(matrix[r][c])
                visited.add((r,c))	
                print(visited)
                print(res)
            
            if not updated:
                    break 

        return res
