class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the brute force solution would start at every
        # number and build a subarray with all the other 
        # numbers proceeding it while updating a "max" variable
        # the runtime for this solution would be n^2

        # The goal is to find a solution faster the n^2 


        # So what we can do is maintain two pointers and create a window
        # We will slide the right pointer and keep track of the sum (updating max when needed)
        # If we find a new lowest sum in relation to the begining we will move the left pointer to the point and reset the sum to 0


        res = None
        start = 0
        end = 0
        currSum = 0 
        height = 0
        prevheight = 0 
        while end < len(nums):
            height += nums[end]
            currSum += nums[end]

            if res:
                res = max(currSum, res)
            else:
                res = nums[end]

            if height < prevheight:
                prevheight = height
                #this is where we shift the left pointer and update the sum
                currSum = 0
                start = end
            end += 1 
            
        return res 
            



        