class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #i: [[5,2],[4,4],[4,1],[3,3]]
        #time: 3
        #res[3, ]
        #process = [enqTime, processTime, index]
        #minHeap = [process, ...]
        
        N = len(tasks)
        processes = []
        for i in range(N):
            processes.append([tasks[i][0],tasks[i][1], i])
        heapq.heapify(processes)
    
        currTime = 0
        res = []
        dueProcesses = []
        while processes or dueProcesses:
            if processes and processes[0][0] > currTime:
                currTime =  currTime = processes[0][0]
            while processes and processes[0][0] <= currTime:
                process = heapq.heappop(processes)
                process = (process[1], process[2]) #(processT, Index)
                heapq.heappush(dueProcesses, process)
            if dueProcesses:
                process = heapq.heappop(dueProcesses)
                currTime += process[0]
                res.append(process[1])
        return res
        
        #i: [[1,2],[2,4],[3,2],[4,1]]

        #processes: [  [3,2, 2], [4,1,3]]
        #time: 5
        #dueProcess: [[2, 2] [4, 1]]
        #res[0,2 ]

