"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True 
        intervals.sort(key = lambda x: x.start) 
        interval = intervals[0]
        for next_interval in intervals[1:]:
            if interval.end > next_interval.start:
                return False 
            interval = next_interval 
        return True 



