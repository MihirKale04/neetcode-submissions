class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(nums: List[int]) -> List[int]:
            n = len(nums)
            if n <= 1:
                return nums
            firstHalf = nums[:n//2]
            secondHalf = nums[n//2:]

            firstHalf = mergesort(firstHalf)
            secondHalf = mergesort(secondHalf)        

            return merge(firstHalf, secondHalf)


        def merge(a1: List[int], a2: List[int]) -> List[int]:
            res = []
            #zipper method 
            p1, p2 = 0, 0
            while p1 < len(a1) and p2 < len(a2):
                if a1[p1] < a2[p2]:
                    res.append(a1[p1])
                    p1 += 1
                else:
                    res.append(a2[p2])
                    p2 += 1
            
            while p1 < len(a1):
                res.append(a1[p1])
                p1 += 1

            while p2 < len(a2):
                res.append(a2[p2])
                p2 += 1

            return res

        return mergesort(nums)      