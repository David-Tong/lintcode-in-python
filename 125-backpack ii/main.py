class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m, a, v):
        # write your code here
        L = len(a)
        # dp[x] - max value of items to hold size x backpack
        dp = [0] * (m + 1)
        for x in range(L):
            for y in range(m, -1, -1):
                if y - a[x] >= 0:
                    dp[y] = max(dp[y], dp[y - a[x]] + v[x])
        return max(dp)


m = 10
a = [2, 3, 5, 7]
v = [1, 5, 2, 4]

m = 10
a = [2, 3, 8]
v = [2, 5, 8]

solution = Solution()
print(solution.back_pack_i_i(m, a, v))
