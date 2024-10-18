class Solution:
    """
    @param s: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotate_string(self, s, offset):
        # write your code here
        L = len(s)
        if L == 0:
            return
        offset = offset % L
        t = s[-1 * offset:] + s[:-1 * offset]

        idx = 0
        while idx < L:
            s[idx] = t[idx]
            idx += 1


s = "abcdefg"
offset = 3

#offset = 0

#offset = 10

solution = Solution()
print(solution.rotate_string(s, offset))
