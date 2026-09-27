class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dpTable = [0] * n
        if n > 2:
            dpTable[0] = nums[0]
            dpTable[1] = max(nums[0], nums[1])
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return nums[0]
        
        for i in range(2, n):
            dpTable[i] = max(dpTable[i - 2] + nums[i], dpTable[i-1])
        

        return dpTable[n-1]
