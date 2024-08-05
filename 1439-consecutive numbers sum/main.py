class Solution:
    """
    @param n: an integer
    @return: how many ways can we write it as a sum of consecutive positive integers
    """
    def consecutive_numbers_sum(self, n):
        # Write your code here
        x = 1
        total = 0

        ans = 0
        while total < n:
            if (n - total) % x == 0:
                ans += 1
            total += x
            x += 1
        return ans


n = 5
n = 9
n = 15
n = 100

solution = Solution()
print(solution.consecutive_numbers_sum(n))
