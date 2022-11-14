class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a):
        # write your code here
        L = len(a)

        if L <= 1:
            return 0

        # dp[y] - the max distance to jump after y + 1 jumps
        dp = [0] * L
        dp[0] = a[0]

        for x in range(1, L):
            for y in range(x - 1, -1, -1):
                if dp[y] >= x:
                    dp[y + 1] = max(dp[y + 1], x + a[x])

        for y in range(L):
            if dp[y] >= L - 1:
                return y + 1
        return -1


A = [2,3,1,1,4]
A = [2]
A = [5,9,3,2,1,0,2,3,3,1,0,0]

solution = Solution()
print(solution.jump(A))
