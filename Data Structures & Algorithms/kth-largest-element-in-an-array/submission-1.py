import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #init heap of size n - k
        # n = len(nums)   
        # minHeap = []
        # for i in range(k):
        #     minHeap.append(nums[i])
        # heapq.heapify(minHeap)
        # for i in range(n - k, n):
        #     heapq.heappush(minHeap, nums[i])
        #     heapq.heappop(minHeap)
        
        # print(minHeap)
        # return heapq.heappop(minHeap)


        n = len(nums)
        minHeap = []
        # negated = [-n for n in nums]
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        for i in range(k, n):
            heapq.heappush(minHeap, nums[i])
            heapq.heappop(minHeap)
        print(minHeap)
        return heapq.heappop(minHeap)

