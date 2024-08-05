class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """
    def insert_five(self, a):
        # write your code here
        if a >= 0:
            positive = True
        else:
            positive = False

        a = str(abs(a))
        L = len(a)
        idx = 0
        while idx < L:
            if positive:
                if a[idx] < '5':
                    break
            else:
                if a[idx] > '5':
                    break
            idx += 1

        ans = int(a[:idx] + "5" + a[idx:])
        if positive:
            return ans
        else:
            return  -1 * ans


a = 234
a = 9765432
a = 97659432
a = -4937
a = -97659432
a = -548
a = -152

solution = Solution()
print(solution.insert_five(a))
