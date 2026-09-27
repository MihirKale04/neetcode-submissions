class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n >= 2:
            return max(self.defaultRob(nums[0:n-1]), self.defaultRob(nums[1:n]))
        return nums[0]

    def defaultRob(self, nums: List[int]) -> int:
        n = len(nums)
        dpTable = [0] *  n
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        else:
            dpTable[0] = nums[0]
            dpTable[1] = max(dpTable[0], nums[1])
            for i in range(2, n):
                dpTable[i] = max(dpTable[i-1], dpTable[i-2] + nums[i]) 
        
        return dpTable[n-1]