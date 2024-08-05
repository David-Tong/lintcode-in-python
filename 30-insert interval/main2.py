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
        start = False
        end = False

        new_start = new_interval.start
        new_end = new_interval.end

        ans = list()
        for interval in intervals:
            if not start:
                if new_interval.start <= interval.start:
                    new_start = new_interval.start
                    start = True
                else:
                    if new_interval.start <= interval.end:
                        new_start = interval.start
                        start = True

            if start and not end:
                if new_interval.end < interval.start:
                    new_end = new_interval.end
                    end = True
                else:
                    if new_interval.end <= interval.end:
                        new_end = interval.end
                        end = True
                        continue

            if not start or end:
                ans.append(interval)

        ans.append(Interval(new_start, new_end))
        ans = sorted(ans, key=lambda x: x.start)
        return ans


intervals = [Interval(1,2), Interval(5,9)]
new_interval = Interval(2, 5)

intervals = [Interval(1,2), Interval(5,9)]
new_interval = Interval(3, 4)

intervals = [Interval(1,2), Interval(5,9)]
new_interval = Interval(0, 10)

intervals = [Interval(1,2), Interval(5,9)]
new_interval = Interval(0, 1)

solution = Solution()
ans = solution.insert(intervals, new_interval)

ans