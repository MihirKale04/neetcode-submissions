class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        N = len(intervals)
        for i in range(0, N - 1):
            #check if overlapping
            first = i
            second = i + 1
            if intervals[first][1] > intervals[second][0]:
                res += 1
                intervals[second][1] = min(intervals[first][1], intervals[second][1])
        return res
        