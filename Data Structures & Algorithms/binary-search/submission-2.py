class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            index = left + ((right - left) // 2)
            if nums[index] == target:
                return index
            if nums[index] > target:
                right = index - 1
            if nums[index] < target:
                left = index + 1
        return -1