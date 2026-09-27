class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        res = float("inf")
        
        for end in range(len(nums)):
            currSum += nums[end]
            
            while currSum >= target:
                res = min(res, end - start + 1)  # Add 1 for length
                currSum -= nums[start]
                start += 1
        
        return res if res != float("inf") else 0

        






        