from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #we start at right most index
        #we simply add the digit we are currently at by one
        #normal we return
        #but if the digit we are at is a 9 we need to turn it to 0 and move the index to the left and repeat the prosses
        digits
        idx = len(digits) - 1 
        while idx >= 0 and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1

        if idx < 0:
            digits = [1] + digits
        else:
            digits[idx] += 1
        return digits