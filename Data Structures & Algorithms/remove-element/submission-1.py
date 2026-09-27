class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        """ My approach """
        counter = 0
        while counter < len(nums):
            print(nums[counter])
            if nums[counter] == val:
                nums.pop(counter)
            else:
                counter += 1
            
        return len(nums)
        

        """ Solution from Neetcode 


        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n

        """