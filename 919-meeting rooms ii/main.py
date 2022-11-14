class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals):
        # Write your code here
        points = list()
        for interval in intervals:
            points.append((interval[0], 1))
            points.append((interval[1], -1))

        points = sorted(points, key=lambda x: (x[0], x[1]))
        print(points)

        ans = 0
        rooms = 0
        for point in points:
            rooms += point[1]
            ans = max(ans, rooms)
        return ans


intervals = [(0,30),(5,10),(15,20)]
intervals = [(2,7)]

solution = Solution()
print(solution.min_meeting_rooms(intervals))
