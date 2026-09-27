"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        #sort intervals
        intervals.sort(key=lambda x: x.start)
        #initialize prev and curr
        for i in range(0, len(intervals) - 1):
            prev = intervals[i].end
            curr = intervals[i + 1].start
            if curr < prev: #found collision
                return False
        return True

        
        
        
        
        # |   |
        #        |                        |P
        #             |c           | false 
    
        
        # start1 end1     start2 end2
        # interval1 with inteval2
        # if start1 < start2 < end1 or start1 < end2 < end1
        


