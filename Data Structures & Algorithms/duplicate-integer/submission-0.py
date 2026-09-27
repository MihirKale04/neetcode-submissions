class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        initlen = len(nums)
        numsSet = set(nums)
        if (initlen != len(numsSet)):
            return True
        else:
            return False
         