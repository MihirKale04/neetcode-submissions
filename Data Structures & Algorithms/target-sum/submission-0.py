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
            
            
            return backTrack(lvl + 1, total + nums[lvl]) + backTrack(lvl + 1, total - nums[lvl])



        return backTrack(0, 0)
        