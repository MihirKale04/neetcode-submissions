class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def FindStartIdx(nums):    
            #We use binary search to find the smallest number 
            start = 0 
            end = len(nums) - 1
            while end > start:
                if nums[start] < nums[end]:
                    return start
                middle = (start + end) // 2
                if nums[middle] < nums[end]:
                    end = middle
                else:
                    start = middle + 1
            return start

        def search(start, end, nums, target):
            while end > start:
                middle = (start + end) // 2
                if nums[middle] == target:
                    return middle
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle
            if nums[start] == target:
                return start
            return -1

        startIdx = FindStartIdx(nums) #return start index

        res = search(0, startIdx - 1, nums, target)
        if res == -1:
            res = search(startIdx, len(nums) -1, nums, target)
        return res