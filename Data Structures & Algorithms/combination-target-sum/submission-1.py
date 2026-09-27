class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We need to do an similar approach to the subset problem
        # where we either choose the number or we don't choose the number
        # we will have to use DFS
        # I guess we will need to pass in the current "sum" while maintaining 
        # a subset with the appropriate numbers
        res = []

        def dfs(index, cur, total):
            if index >= len(nums) or total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[index])
            dfs(index, cur, total + nums[index])

            cur.pop()
            dfs(index + 1,cur, total)
        
        dfs(0,[], 0)
        return res
        