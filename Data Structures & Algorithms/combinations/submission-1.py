class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(num, count, arr):
            if count == k:
                res.append(arr.copy())
                return
            for i in range(num, n + 1):
                arr.append(i)
                dfs(i + 1, count + 1, arr)
                arr.pop()
        dfs(1, 0, [])
        return res