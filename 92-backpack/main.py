class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m, a):
        # write your code here
        # dp[x] - if we can place backpack with size x
        dp = [False] * (m + 1)
        dp[0] = True
        for item in a:
            for x in range(m, -1, -1):
                if x - item >= 0:
                    if dp[x - item]:
                        dp[x] = True

        for x in range(m, -1, -1):
            if dp[x]:
                return x


m = 10
a = [3,4,8,5]

m = 12
a = [2,3,5,7]

solution = Solution()
print(solution.back_pack(m, a))
