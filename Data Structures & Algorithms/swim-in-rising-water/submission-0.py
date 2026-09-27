class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0 ,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))
        while minHeap: 
            time, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1: 
                return time     
            for dr, dc in directions:
                neigR, neigC = r + dr, c + dc
                #bounds check
                if (neigR < 0 or neigC < 0 or neigR == N or neigC == N or (neigR, neigC) in visit):
                    continue
                visit.add((neigR, neigC))
                heapq.heappush(minHeap, [max(time, grid[neigR][neigC]), neigR, neigC])
