import sys
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums))
        dp[-1] = 1
        
        for i in range(len(nums) - 2, -1, -1):
            maxval = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    if dp[j] + 1 > maxval:
                        maxval = dp[j] + 1
            dp[i] = maxval
        return max(dp)
