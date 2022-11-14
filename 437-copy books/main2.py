class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages, k):
        # write your code here
        N = len(pages)
        if N == 0:
            return 0

        prefixes = [0] * (N + 1)
        for y in range(1, N + 1):
            prefixes[y] = prefixes[y - 1] + pages[y - 1]

        # dp[x][y] - the minimal time to copy book y book with x people
        dp = [[float("inf")] * N for _ in range(k)]
        for x in range(k):
            for y in range(N):
                # x == 0, only 1 people to copy all books
                # time needed to the sum of book pages
                if x == 0:
                    dp[0][y] = prefixes[y + 1]

                # y == 0, only 1 book to copy
                # time needed to copy page is the time for all the pages in the book 0
                elif y == 0:
                    dp[x][0] = pages[0]

                # dp formula
                else:
                    for z in range(y + 1):
                        dp[x][y] = min(dp[x][y], max(dp[x - 1][y - z], prefixes[y + 1] - prefixes[y + 1 - z]))

        return dp[k - 1][N - 1]


pages = [3, 2, 4]
k = 2

pages = [3, 2, 4]
k = 3

solution = Solution()
print(solution.copy_books(pages, k))
