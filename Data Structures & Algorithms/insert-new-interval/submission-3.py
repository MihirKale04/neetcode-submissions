class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Two steps
        #Step 1: Identify where the intervals needs to be inserted
            #loop through intervals and find the appropriate spot O(n)

        #Step 2: Merge accordingly
            #observation 1: No Merge 
                #- no collision between prev newInt next
                # |    |         |     | original
                #        |     |    newInt
            #observation 2: Prev Next merged
                #- newInt collides both prev and next
                # prevStart < newIntStart and nextEnd > newIntEnd
                # |    | |     | original
                #     |     |    newInt
            #observation 3:
                # |    |      |     | original
                #     |               |    newInt
            #observation 4:
                #       |    | |     | original
                #     |          |    newInt
            #observation 5:
                 #       |    | |     | original
                #     |                        |    newInt
            #------------
                #   |   |    |    | |     |      |   |      original
                #     |                        |    newInt
            #prev Interval: interval right before newIntStart
            #next Interval: Interval right after the newIntend
            #intervals inbetween: all Intervals in between newIntStart and newIntEnd
            
            #[[1, 5], [8, 18], [30, 55]]

            #newInterval = [8, 18]
        if not intervals:
            return [newInterval]
        
        res = []
        added = False
        for i in range(len(intervals)):
            if not added:
                if intervals[i][0] > newInterval[0]: #not newInt
                    #add newInterval
                    if res and res[-1][1] >= newInterval[0]:
                        res[-1][1] = max(newInterval[1], res[-1][1])
                    else:
                        res.append(newInterval)
                    added = True
            if res and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        if not added:
            if res and res[-1][1] >= newInterval[0]:
                res[-1][1] = max(newInterval[1], res[-1][1])
            else:
                res.append(newInterval)
        return res
      