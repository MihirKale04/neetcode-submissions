class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #we can iter through the linked list
        #add each number to a set
        #when ever we apporach a number that appears in the set alr return that number
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1 
        