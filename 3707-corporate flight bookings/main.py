class Solution:
    """
    @param bookings: Flight booking information
    @param n: Total number of flights
    @return: Number of seats booked per flight
    """
    def corp_flight_bookings(self, bookings, n):
        # write your code here
        # pre-process
        diffs = [0] * n
        for booking in bookings:
            start, end, seats = booking
            diffs[start - 1] += seats
            if end < n:
                diffs[end] -= seats

        # process
        ans = list()
        for idx in range(n):
            if idx == 0:
                ans.append(diffs[idx])
            else:
                ans.append(ans[-1] + diffs[idx])
        return ans


bookings = [[1,2,10],[2,4,20],[2,5,25]]
n = 5

bookings = [[1,2,10],[2,2,20]]
n = 2

solution = Solution()
print(solution.corp_flight_bookings(bookings, n))
