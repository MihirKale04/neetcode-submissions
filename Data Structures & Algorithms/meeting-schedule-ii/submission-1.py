"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #core of the problem:
            #To determine  the maximum amount of intervals that overlap at a given moment
        N = len(intervals)
        
        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)

        startTimes.sort()
        endTimes.sort()

        sIdx = 0
        eIdx = 0

        maxCount = 0
        count = 0      
        
        while sIdx < N and eIdx < N:
            if startTimes[sIdx] < endTimes[eIdx]:
                count += 1
                sIdx += 1
            else:
                count -= 1
                eIdx += 1
            maxCount = max(count, maxCount)
        return maxCount