import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for ch, count in freq.items(): 
            heapq.heappush(heap, (-count, ch))
        res = ""
        #build string by flushing heap
        prev = None
        while heap:
            count, ch = heapq.heappop(heap)
            if ch == prev:
                print("condition hit")
                #take the next
                if heap:
                    tempCount, tempCh = heapq.heappop(heap)
                    heapq.heappush(heap, (count, ch))
                    count, ch = tempCount, tempCh
                else:
                    return ""
            #process
            count += 1
            res += ch
            prev = ch
            print(count, ch)
            if count < 0:
                heapq.heappush(heap, (count, ch))
        return res      