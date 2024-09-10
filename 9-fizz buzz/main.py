class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizz_buzz(self, n):
        # write your code here
        def is_divisible(dividend, divisor):
            return True if dividend % divisor == 0 else False

        ans = list()
        for x in range(n):
            if is_divisible(x + 1, 15):
                ans.append("fizz buzz")
            elif is_divisible(x + 1, 5):
                ans.append("buzz")
            elif is_divisible(x + 1, 3):
                ans.append("fizz")
            else:
                ans.append(str(x + 1))
        return ans


n = 15
solution = Solution()
print(solution.fizz_buzz(n))
