class Solution:
    def __init__(self):
        from collections import defaultdict
        self.events = defaultdict(list)

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        def get_bound_second(timestamp, rate):
            _, unit = rate.split("/")
            if unit == "s":
                interval = 1
            elif unit == "m":
                interval = 60
            elif unit == "h":
                interval = 60 * 60
            elif unit == "d":
                interval = 60 * 60 * 24

            return max(0, timestamp - interval)

        def is_rate_limited(event, rate, bound):
            rates, _ = rate.split("/")
            records = self.events[event]

            from bisect import bisect_right
            idx = bisect_right(records, bound)

            if len(records) - idx >= int(rates):
                return True
            else:
                return False

        bound = get_bound_second(timestamp, rate)
        limited = is_rate_limited(event, rate, bound)
        if limited:
            return True
        else:
            if increment:
                self.events[event].append(timestamp)
            return False


solution = Solution()
print(solution.isRatelimited(1, "login", "3/m", True))
print(solution.isRatelimited(11, "login", "3/m", True))
print(solution.isRatelimited(21, "login", "3/m", True))
print(solution.isRatelimited(30, "login", "3/m", True))
print(solution.isRatelimited(65, "login", "3/m", True))
print(solution.isRatelimited(300, "login", "3/m", True))
