class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def is_happy(self, n):
        # write your code here
        from collections import defaultdict
        self.cache = defaultdict(str)

        def check_happy(digits):
            if digits in self.cache:
                return False

            total = 0
            for digit in digits:
                total += int(digit) ** 2
            if total == 1:
                return True
            else:
                self.cache[digits] = total
                return check_happy(str(total))

        return check_happy(str(n))


n = 19
n = 5

solution = Solution()
print(solution.is_happy(n))
