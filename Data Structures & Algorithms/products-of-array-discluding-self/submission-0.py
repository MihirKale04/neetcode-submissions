class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        res = []
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            prefix.append(prod)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suffix[i] = prod
        
        for i in range(len(nums)):
            if i == 0:
                res.append(1 * suffix[i + 1])
            elif i == len(nums) - 1:
                res.append(1 * prefix[i - 1])
            else:
                res.append(prefix[i - 1] * suffix[i + 1])
        
        return res
        
        