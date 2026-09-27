import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        res = 0
        first = 0
        second = 0
        while second < len(prices):
            if prices[second] < minPrice:
                minPrice = prices[second]
                first = second
            res = max(prices[second] - prices[first], res)

            second += 1 
        return res
        