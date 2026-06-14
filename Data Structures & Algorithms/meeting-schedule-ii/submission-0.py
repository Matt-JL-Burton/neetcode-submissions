"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        start_times = {}
        end_times = {}
        times = set()
        for i in range(len(intervals)):
            start_times[intervals[i].start] = start_times.get(intervals[i].start, 0) + 1
            end_times[intervals[i].end] = end_times.get(intervals[i].end, 0) + 1
            times.add(intervals[i].start)
            times.add(intervals[i].end)


        sorted_times = sorted(times)

        max_rooms = 0
        current_rooms = 0
        for time in sorted_times:
            number_of_opened_rooms = start_times.get(time, 0)
            number_of_closed_rooms = end_times.get(time, 0)
            current_rooms = current_rooms + number_of_opened_rooms - number_of_closed_rooms
            max_rooms = max(max_rooms, current_rooms)
        
        return max_rooms
                

