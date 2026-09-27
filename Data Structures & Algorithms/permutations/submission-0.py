class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        intRemaining = nums

        def backtrace(intRemaining, permutation):
            if len(intRemaining) == 0:
                print("permuation added to result")
                res.append(permutation.copy())
                return
            
            for i in range(len(intRemaining)):
                integer = intRemaining[i]
                permutation.append(integer)
                intRemaining.pop(i)
                print (i, intRemaining, permutation,  "before")
                backtrace(intRemaining, permutation)
                permutation.pop()
                intRemaining.insert(i, integer)
                print (i, intRemaining, permutation, "after")
                
        backtrace(intRemaining, permutation)
        return res

