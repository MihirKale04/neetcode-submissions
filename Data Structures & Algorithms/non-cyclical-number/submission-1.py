class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        sums = set()
        sums.add(n)
        currNum = n
        while True:
            tot = 0
            while currNum > 0:
                dig = currNum % 10
                tot += dig ** 2
                currNum = currNum // 10    
            currNum = tot
            if currNum in sums:
                return False
            if currNum == 1:
                return True
            sums.add(currNum)
