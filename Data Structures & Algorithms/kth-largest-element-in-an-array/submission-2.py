import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minHeap = []
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        for i in range(k, n):
            heapq.heappush(minHeap, nums[i])
            heapq.heappop(minHeap)
        print(minHeap)
        return heapq.heappop(minHeap)

