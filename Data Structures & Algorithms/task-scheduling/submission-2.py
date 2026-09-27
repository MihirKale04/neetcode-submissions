import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #maybe we create a hashmap storing the count of each unique task
        #based on the count we create a maxheap
        #we pop the top of the heap n times 
            #if the heap is empty before n counts we fill with idle
            #while we pop we decrement the count of heap
        #we repeat this process until the count for all tasks is 0 
        #when the count is zero we can remove that task from our hashmap

        #initialize a hashmap for count of tasks
        taskCount = Counter(tasks)
        
        #inititalize heap
        heap = []
        for task in taskCount:
            heapq.heappush(heap, -taskCount[task])
        Q = deque()
        res = 0
        while heap or Q:
            res += 1
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    Q.append((count, res + n))
            # else:
            #     res = Q[0][1]
    
            if Q and Q[0][1] == res:
                heapq.heappush(heap, Q.popleft()[0]) 
            
            

        return res
        