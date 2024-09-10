class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def first_will_win(self, values):
        # write your code here
        # pre-process
        L = len(values)
        from collections import defaultdict
        cache = defaultdict(int)

        def take(idx):
            # cache
            key = idx
            if key in cache:
                return cache[key]

            # have taken all
            if idx >= L:
                return 0
            # go to take all
            if idx >= L - 2:
                return sum(values[idx:])

            # dp min-max
            min_max = float("-inf")
            curr = 0
            for x in range(2):
                curr += values[idx + x]
                min_max = max(min_max, curr - take(idx + 1 + x))

            # set cache
            if key not in cache:
                cache[key] = min_max

            return min_max

        # process
        return True if take(0) >= 0 else False


values = [1, 2, 2]
values = [1, 2, 4]
values = [1, 2, 3]

solution = Solution()
print(solution.first_will_win(values))
