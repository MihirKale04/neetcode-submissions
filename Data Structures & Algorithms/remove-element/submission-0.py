class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        while counter < len(nums):
            print(nums[counter])
            if nums[counter] == val:
                nums.pop(counter)
            else:
                counter += 1
            
        return len(nums)
        