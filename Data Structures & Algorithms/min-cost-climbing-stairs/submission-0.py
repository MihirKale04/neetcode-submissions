class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dpTable = [0] * n
        dpTable[0] = cost[n - 1]
        dpTable[1] = cost[n - 2]
        for i in range (0, n - 2):
            dpTable[2 + i] = cost[n - 3 - i] + min(dpTable[1 + i], dpTable[i])
        return min(dpTable[n - 1], dpTable[n - 2])     