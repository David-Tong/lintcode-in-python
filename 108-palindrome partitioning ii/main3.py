class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s):
        # write your code here
        # pre-process
        L = len(s)

        # helper function
        def is_palindrome(x, y):
            left, right = x, y
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # do min cut for s[x:]
        def do_min_cut(start):
            if start in cache:
                return cache[start]
            if is_palindrome(start, L - 1):
                return 0
            min_cut = float("inf")
            for x in range(start, L):
                if is_palindrome(start, x):
                    min_cut = min(min_cut, do_min_cut(x + 1) + 1)
            cache[start] = min_cut
            return min_cut

        from collections import defaultdict
        cache = defaultdict(int)
        return do_min_cut(0)


s = "a"
s = "aab"
s = "abacabac"

solution = Solution()
print(solution.min_cut(s))