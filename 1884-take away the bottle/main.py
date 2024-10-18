class Solution:
    """
    @param arr: the array of bottles
    @return: the minimum number of times you can take all the bottles
    """
    def take_away_the_bottle(self, arr):
        # Write your code here.
        # dp init
        L = len(arr)
        print(L)
        dp = [[float("inf")] * L for _ in range(L)]
        # calculate interval range of 1
        for x in range(L):
            dp[x][x] = 1
        # calculate interval range of 2
        for x in range(L - 1):
            if arr[x] == arr[x + 1]:
                dp[x][x + 1] = 1
            else:
                dp[x][x + 1] = 2

        # dp transfer
        for l in range(3, L + 1):
            for x in range(L - l + 1):
                y = x + l - 1
                # print(x, y)
                if arr[x] == arr[y]:
                    dp[x][y] = dp[x + 1][y - 1]
                for k in range(x + 1, y + 1):
                    dp[x][y] = min(dp[x][y], dp[x][k - 1] + dp[k][y])

        # dp result
        return dp[0][L - 1]


arr = [1,3,4,1,5]
arr = [1,2,3,5,3,1]
arr = [1,2,2,2,2,1,2,1,1,2,1]
arr = [93,42,50,40,40,50,90,78,84,45,95,95,45,84,78,57,69,15,15,12,14,85,12,62,31,77,31,62,12,85,12,15,15,60,53,60,69,57,90,42,93]

solution = Solution()
print(solution.take_away_the_bottle(arr))
