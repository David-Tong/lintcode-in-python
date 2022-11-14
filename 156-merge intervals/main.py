class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if len(intervals) == 0:
            return list()

        intervals = sorted(intervals, key=lambda x : (x.start,  -1 * x.end))
        start = intervals[0].start
        end = intervals[0].end
        ans = list()
        for interval in intervals[1:]:
            if interval.start <= end:
                if interval.end > end:
                    end = interval.end
            else:
                ans.append(Interval(start, end))
                start = interval.start
                end = interval.end
        ans.append(Interval(start, end))
        return ans


intervals = list()
intervals.append(Interval(1, 3))

"""
intervals.append(Interval(1, 3))
intervals.append(Interval(1, 6))
intervals.append(Interval(2, 6))
intervals.append(Interval(8, 10))
intervals.append(Interval(15, 18))
"""

solution = Solution()
print(solution.merge(intervals))
