"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.end)
        n=len(intervals)
        if n <= 1:
            return True
        end = intervals[0].end
        n = len(intervals)
        for i in range(1,n):
            if intervals[i].start < end:
                return False
            end = intervals[i].end
        return True
