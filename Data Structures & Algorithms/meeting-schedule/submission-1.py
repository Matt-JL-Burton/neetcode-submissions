"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        busy = False
        sp, ep = 0, 0
        while sp < len(start) and ep < len(end):
            if start[sp] >= end[ep]:
                ep += 1
                busy = False
            else:
                sp += 1
                if busy:
                    return False
                busy = True
        
        return True
