import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.heap = nums[-k:]
        heapq.heapify(self.heap)
        print(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
            print(self.heap)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
        
