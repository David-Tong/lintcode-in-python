class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizz_buzz(self, n):
        # write your code here
        ans = list()
        for x in range(n):
            if (x + 1) % 15 == 0:
                ans.append("fizz buzz")
            elif (x + 1) % 5 == 0:
                ans.append("buzz")
            elif (x + 1) % 3 == 0:
                ans.append("fizz")
            else:
                ans.append(str(x + 1))
        return ans


n = 15

solution = Solution()
print(solution.fizz_buzz(n))
