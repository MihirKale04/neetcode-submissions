import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        #We need a DP table that stores two things: min and max product up to that point.
        dp = [[1, 1] for _ in range(n + 1)]
        res = -sys.maxsize-1
        for i in range (1 , n + 1):
            #TODO: define dp recurrence relation
            dp[i][0] = max(nums[i -1] * dp[i - 1][0], nums[i -1] * dp[i - 1][1], nums[i - 1])
            dp[i][1] = min(nums[i -1] * dp[i - 1][0], nums[i -1] * dp[i - 1][1], nums[i - 1])
            print(dp[i], nums[i-1], dp[i-1])
            res = max(res, dp[i][0])
        return res