import heapq
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
        taskCount = {}
        for task in tasks:
            taskCount[task] = 1 + taskCount.get(task, 0)
        
        #inititalize heap
        heap = []
        for task in taskCount:
            heapq.heappush(heap, (-taskCount[task], task))
        
        res = 0
        while taskCount:
            cycles = n
            while cycles >= 0:
                if heap:
                    count, task = heapq.heappop(heap)
                    taskCount[task] -= 1
                    # print(task)
                    if taskCount[task] == 0:
                        del taskCount[task]
                # else:
                #     print("idle")
                res += 1
                if not taskCount: #break early if we exhausted through all tasks
                    break
                cycles -= 1 
            #rebuild heap
            heap = []
            for task in taskCount:
                heapq.heappush(heap, (-taskCount[task], task))
        

        return res
        