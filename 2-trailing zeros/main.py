class Solution:
    """
    @param n: A long integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailing_zeros(self, n):
        # write your code here
        idx = 1
        ans = 0
        while 5 ** idx <= n:
            ans += n // (5 ** idx)
            idx += 1
        return ans

n = 5
n = 11

solution = Solution()
print(solution.trailing_zeros(n))
