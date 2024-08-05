class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meeting_room_i_i_i(self, intervals, rooms, ask):
        # Write your code here.
        # pre-process
        L = len(ask)
        schedules = list()
        for interval in intervals:
            start, end = interval
            schedules.append((start, -1))
            schedules.append((end, 1))
        schedules = sorted(schedules, key=lambda x: (x[0], -x[1]))

        from collections import defaultdict
        dicts = defaultdict(int)
        dicts[0] = rooms
        for schedule in schedules:
            time, offset = schedule
            rooms += offset
            dicts[time] = rooms
        # print(dicts)

        unavailables = list()
        start = -1
        for key in sorted(dicts.keys()):
            if dicts[key] == 0:
                if start == -1:
                    start = key
            else:
                end = key
                if start != -1:
                    unavailables.append((start, end))
                    start = -1
        U = len(unavailables)
        # print(unavailables)

        # process
        from bisect import bisect_left
        ans = [True] * L
        for idx, ak in enumerate(ask):
            start, end = ak
            idx_start = bisect_left(unavailables, (start, start))
            if idx_start < U:
                if end > unavailables[idx_start][0]:
                    ans[idx] = False
            if  idx_start > 0:
                if start < unavailables[idx_start - 1][1]:
                    ans[idx] = False
        return ans


intervals = [[1,2],[4,5],[8,10]]
rooms = 1
ask = [[2,3],[3,4]]

intervals = [[1,2],[4,5],[8,10]]
rooms = 1
ask = [[4,5],[5,6]]

intervals = [[1,2],[4,5],[8,10]]
rooms = 1
ask = [[0,1],[2,3],[3,4],[10,11],[11,12]]

intervals = [[1,2],[1,3],[3,4],[4,5],[8,10]]
rooms = 2
ask = [[2,4]]

intervals = [[1,3],[4,6],[6,8],[9,11],[6,9],[1,3],[4,10]]
rooms = 3
ask = [[1,9],[2,6],[7,9],[3,5],[3,9],[2,4],[7,10],[5,9],[3,10],[9,10]]

intervals = [[4,11],[1,4],[4,6],[6,8],[8,11],[1,6],[6,8],[9,11]]
rooms = 3
ask = [[6,10],[7,10],[6,9],[6,7],[9,10],[7,10],[4,8],[8,9],[1,10],[7,10]]

intervals = [[1,3],[3,6],[10,13],[13,15],[15,17],[1,3],[3,5],[5,7],[7,9],[9,11],[12,15],[15,17],[17,19],[19,21],[2,4],[4,6],[6,8],[9,12],[12,14],[14,16],[17,19],[19,21],[2,5],[5,7],[7,9],[9,11],[11,13],[13,15],[15,17],[17,19],[9,19]]
rooms = 5
ask = [[17,18],[13,15],[3,18],[13,14],[6,15],[2,10],[7,10],[11,17],[6,16],[10,16],[11,19],[18,20],[10,12],[3,7],[5,15],[12,19],[16,19],[11,19],[16,19],[7,8]]

solution = Solution()
print(solution.meeting_room_i_i_i(intervals, rooms, ask))
