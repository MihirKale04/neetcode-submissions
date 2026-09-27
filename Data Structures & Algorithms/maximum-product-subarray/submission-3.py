import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[]] * (n + 1)
        res = -sys.maxsize - 1
        for i in range(1, n+1):
            prevArr = dp[i - 1]
            newArr = []
            for val in prevArr:
                newArr.append(val* nums[i - 1])
            newArr.append(nums[i-1])
            dp[i] = newArr
            res = max(res, max(dp[i]))
        return res