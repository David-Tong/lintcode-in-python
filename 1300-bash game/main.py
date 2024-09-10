class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n):
        # Write your code here
        return False if n % 4 == 0 else True

n = 10000

solution = Solution()
print(solution.can_win_bash(n))
