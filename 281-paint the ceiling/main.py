class Solution:
    """
    @param s0: the number s[0]
    @param n: the number n
    @param k: the number k
    @param b: the number b
    @param m: the number m
    @param a: area
    @return: the way can paint the ceiling
    """
    def paintthe_ceiling(self, s0, n, k, b, m, a):
        # write your code here
        # pre-process
        s = [s0]
        for x in range(1, n):
            s1 = ((k * s[-1] + b) % m) + 1 + s[-1]
            if s1 * s0 > a:
                break
            s.append(s1)

        # process
        # two-points
        print(len(s))
        print(s[-1])
        left = 0
        right = len(s) - 1

        ans = 0
        while left <= right:
            if s[left] * s[right] <= a:
                ans += (right - left) * 2 + 1
                left += 1
            else:
                right -= 1
        return ans


s_0 = 2
n = 3
k = 3
b = 3
m = 2
a = 15

s_0 = 3
n = 200
k = 3
b = 3
m = 2
a = 15000

s_0 = 3
n = 6 * 10 ** 6
k = 3
b = 3
m = 2
a = 10 ** 18

solution = Solution()
print(solution.paintthe_ceiling(s_0, n, k, b, m, a))
