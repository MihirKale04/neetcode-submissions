class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we need to do a backtrace where we build an num array and
        # append when the sum of the num array is equal to the target
        # or throw away the num array when the sum in more the target
        
        res = []
        numArray = []
        numArraySum = 0
        def backtrace(index, numArray, numArraySum):
            if numArraySum > target:
                return
            if numArraySum == target:
                res.append(numArray.copy())
            
            for i in range(index, len(nums), 1):
                numArray.append(nums[i])
                numArraySum += nums[i]
                backtrace(i,numArray,numArraySum)
                numArray.pop()
                numArraySum -= nums[i]
        backtrace(0, numArray, numArraySum)
        return res

                
            
        