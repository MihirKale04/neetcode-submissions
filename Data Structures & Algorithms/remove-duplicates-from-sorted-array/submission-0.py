class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:     
        left = 0
        right = left + 1
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                nums.pop(right)
            left = right
            right = left + 1

        return len(nums)

        