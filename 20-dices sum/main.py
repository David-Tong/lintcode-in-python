class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        # dp init
        # dp[x] - the number of chance to have sum of x
        L = 6 * n + 1
        dp = [0] * L
        dp[0] = 1

        # dp transfer
        for z in range(n):
            prev = dp
            dp = [0] * L
            for x in range(1, L):
                for y in range(1, 7):
                    if x - y >= 0:
                        dp[x] += prev[x - y]

        # post process
        total = sum(dp)
        ans = list()
        for idx, c in enumerate(dp):
            if c > 0:
                ans.append((idx, c * 1.0 / total))
        return ans


n = 1
n = 2

solution = Solution()
print(solution.dicesSum(n))
