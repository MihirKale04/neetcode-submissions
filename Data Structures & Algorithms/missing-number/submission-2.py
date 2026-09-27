class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #hacky method
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] != count:
        #         return count
        #     count += 1
        # return -1        
        

        # """this might be wrong but we could sum up all the numbers and iteratively xor from 0 to n
        # the result may be the missing number"""
        # total = 0
        # for num in nums:
        #     total += num
        # for i in range(len(nums)):
        #     total = total ^ i
        # return total

        xor = 0
        for i in range(1, len(nums) + 1):
            xor = xor ^ i
        
        for num in nums:
            xor = xor ^ num


        return xor
        