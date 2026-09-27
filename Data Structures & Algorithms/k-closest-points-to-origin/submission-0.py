import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """We are going to pass through the array and calc
        the euclidean distance O(n)"""

        """We need to create a maxHeap of size k"""
        """On every iteration we pop from the heap (remove the max)"""
        """By the end we should be left with the smallest k distances"""

        """Ok I may need to create my own heap data structure to solve this problem"""
        
        
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)    
        res = []
        for i in range (k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res