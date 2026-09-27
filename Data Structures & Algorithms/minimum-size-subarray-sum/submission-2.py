class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        currSum = 0
        n = len(nums)
        res = float("inf")
        while end < n:
            while currSum >= target:
                res = min(res, end - start)
                currSum -= nums[start]
                start += 1
            currSum += nums[end]
            end += 1
        
        while currSum >= target:
                res = min(res, end - start)
                currSum -= nums[start]
                start += 1

        if res == float('inf'):
            return 0
        return res

        






        