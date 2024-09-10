class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n):
        # Write your code here
        from collections import defaultdict
        cache = defaultdict(bool)

        def take(stones):
            if stones in cache:
                return cache[stones]

            if stones <= 3:
                return True
            win = True
            for x in range(3):
                win &= take(stones - 1 - x)

            cache[stones] = win
            return not win

        ans = take(n)
        print(cache)
        return ans


n = 4
n = 5
n = 10000

solution = Solution()
print(solution.can_win_bash(n))
