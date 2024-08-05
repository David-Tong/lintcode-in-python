"""
from lintcode import (
    Interval,
)
"""
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: Sorted interval list.
    @param new_interval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, new_interval):
        # write your code here
        # pre-process
        intervals.append(new_interval)
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))

        # process
        start = intervals[0].start
        end = intervals[0].end
        ans = list()
        for interval in intervals[1:]:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                ans.append(Interval(start, end))
                start = interval.start
                end = interval.end
        ans.append(Interval(start, end))
        return ans


intervals = [Interval(1, 2), Interval(5, 9)]
new_interval = Interval(2, 5)

intervals = [Interval(1, 2), Interval(5, 9)]
new_interval = Interval(3, 4)

intervals = [Interval(1, 2), Interval(5, 9)]
new_interval = Interval(0, 10)

intervals = [Interval(1, 2), Interval(5, 9)]
new_interval = Interval(0, 1)

solution = Solution()
ans = solution.insert(intervals, new_interval)

ans