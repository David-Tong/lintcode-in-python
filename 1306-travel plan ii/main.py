class Solution:
    """
    @param arr: the distance between any two cities
    @return: the minimum distance Alice needs to walk to complete the travel plan
    """
    def travel_plan_i_i(self, arr):
        # Write your code here.
        # pre-process
        L = len(arr)
        S = 1 << L

        # init dp
        dp = [[float("inf")] * L for _ in range(S)]
        dp[1][0] = 0

        # process
        # dp transfer
        for s in range(1, S):
            # start city x
            for x in range(L):
                # skip start city x since it has not been visited
                if (s >> x) & 1:
                    # end city y
                    for y in range(1, L):
                        # next state, skip end city if it has been visited
                        if not ((s >> y) & 1):
                            ns = s | (1 << y)
                            dp[ns][y] = min(dp[ns][y], dp[s][x] + arr[x][y])
        # print(dp)

        # post-process
        ans = float("inf")
        for x in range(1, L):
            ans = min(ans, dp[S - 1][x] + arr[x][0])
        return ans


arr = [[0,1,2],[1,0,2],[2,1,0]]
arr = [[0,10000,2],[5,0,10000],[10000,4,0]]
arr = [[0,35,45,12,30],[55,0,20,30,50],[30,20,0,10,100],[20,30,50,0,120],[20,50,70,85,0]]

solution = Solution()
print(solution.travel_plan_i_i(arr))
