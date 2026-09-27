class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #(lvl, sum) -> number of ways to hit the target
        dp = {}
        def backTrack(lvl, total):
            if lvl == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (lvl, total) in dp:
                return dp[lvl, total]
            result = backTrack(lvl + 1, total + nums[lvl]) + backTrack(lvl + 1, total - nums[lvl])
            dp[(lvl, total)] = result
            return result


        return backTrack(0, 0)
        