class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            hoursNeeded = 0

            for pile in piles:
                hoursNeeded += math.ceil(pile/mid)

            if hoursNeeded <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            print (hoursNeeded, ans)
        return ans
    
        
        



        
        