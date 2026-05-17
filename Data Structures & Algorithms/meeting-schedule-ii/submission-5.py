"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        if n == 0 or n == 1:
            return n
        pq = []
        heapq.heappush(pq, intervals[0].end)
        for i in range(1,n):
            if intervals[i].start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, intervals[i].end) 
        return len(pq)