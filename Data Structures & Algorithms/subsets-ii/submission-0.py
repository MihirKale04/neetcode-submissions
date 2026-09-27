class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        stack = []
    
        def backtrack(stack, pos, fresh):
            res.append(stack.copy())
            print("stack on this step:", stack)
            print("nums we are wroking with", nums[pos:])
            for i in range(pos,len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not fresh:
                    print("skipped")
                    continue
                fresh = False
                print("append:", nums[i])
                stack.append(nums[i])
                backtrack(stack, i + 1, fresh=True)
                stack.pop()



        backtrack(stack, 0,True)
        return res

        