class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    def back_pack_i_i_i(self, a, v, m):
        # write your code here
        L = len(a)

        # dp[x] - max value for the backpack with size x
        dp = [0] * (m + 1)

        for x in range(m + 1):
            for y in range(L):
                if x - a[y] >= 0:
                    dp[x] = max(dp[x], dp[x - a[y]] + v[y])
        return max(dp)


A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
m = 10

A = [1, 2, 3]
V = [1, 2, 3]
m = 5

solution = Solution()
print(solution.back_pack_i_i_i(A, V, m))
