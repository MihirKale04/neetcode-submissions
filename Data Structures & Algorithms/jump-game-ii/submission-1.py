class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        idx = 0
        seek = nums[idx]
        res = 0 
        while True:
            offset = 0
            options = []
            for i in range(seek):
                idx += 1 
                offset += 1
                if idx == len(nums) - 1:
                    return res + 1
                options.append((nums[idx] + offset, idx))
            res += 1
            maxSeek, idx = max(options)
            seek = nums[idx]
        return res


        