class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a):
        # write your code here
        dp = [False] * len(a)
        dp[0] = True
        for x in range(1, len(a)):
            for y in range(x):
                if dp[y] and x - y <= a[y]:
                    dp[x] = True
        return dp[len(a) - 1]


a = [2, 3, 1, 1, 4]
#a = [3, 2, 1, 0, 4]
#a = [0, 8, 2, 0, 9]

solution = Solution()
print(solution.can_jump(a))
