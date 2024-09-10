class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digit_counts(self, k, n):
        # write your code here
        # process
        ans = 0
        for x in range(n + 1):
            for d in str(x):
                if int(d) == k:
                    ans += 1
        return ans


k = 1
n = 1

k = 1
n = 12

k = 9
n = 99

k = 9
n = 999

"""
k = 9
n = 45990
"""

solution = Solution()
print(solution.digit_counts(k, n))
