import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones] #this will be an O(n) runtime
        heapq.heapify(stones) #heapify stones will have an O(n) runtime
        while stones: # this will run at most n times   
            if len(stones) == 1:
                return -stones[0]
            elif len(stones) >= 2:
                y = -heapq.heappop(stones) #This operation has a runtime of O(logn)
                x = -heapq.heappop(stones) #This operation has a runtime of O(logn)
                if x == y:
                    continue
                elif x < y:
                    heapq.heappush(stones,-(y - x)) #This operation has a runtime of O(logn)        
        return 0
        #Total runtime of Algo will Be(nlogn) outside loop runs at most n times while inside operations such as heappop and push have internal runtimes of logn
       
