class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = []
        def backtracking(index):
            if index >= len(nums):
                res.append(stack.copy())
                return
            
            stack.append(nums[index])
            backtracking(index + 1)

            stack.pop()
            backtracking(index + 1)

        backtracking(0)
        return res
            