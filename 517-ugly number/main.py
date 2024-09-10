class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def is_ugly(self, num):
        # write your code here
        def divide_by_n(num, n):
            while num % n == 0:
                num //= n
            return num

        # check
        if num == 0: return False
        for divisor in [5, 3, 2]:
            num = divide_by_n(num , divisor)

        return True if num == 1 else False


num = 0
num = 8
num = 9756567

solution = Solution()
print(solution.is_ugly(num))
