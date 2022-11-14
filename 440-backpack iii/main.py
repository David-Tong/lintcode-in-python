class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    def back_pack_i_i_i(self, a, v, m):
        # write your code here
        dp = [-1] * (m + 1)
        dp[0] = 0

        for x in range(m + 1):
            for idx, size in enumerate(a):
                if x - size >= 0 and dp[x - size] >= -1:
                    dp[x] = max(dp[x], dp[x - size] + v[idx])

        return max(dp)


a = [2,3,5,7]
v = [1,5,2,4]
m = 10

a = [1,2,3]
v = [1,2,3]
m = 5

solution = Solution()
print(solution.back_pack_i_i_i(a, v, m))
