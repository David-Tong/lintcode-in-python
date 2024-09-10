class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n):
        # write your code here
        # pre-process
        uglies = list()
        ugly = 1
        uglies.append(ugly)
        idx2, idx3, idx5 = 0, 0, 0

        # process
        while len(uglies) < n:
            ugly2 = uglies[idx2] * 2
            ugly3 = uglies[idx3] * 3
            ugly5 = uglies[idx5] * 5

            ugly = min(ugly2, min(ugly3, ugly5))
            if ugly not in uglies:
                uglies.append(ugly)
            if ugly2 == ugly:
                idx2 += 1
            elif ugly3 == ugly:
                idx3 += 1
            elif ugly5 == ugly:
                idx5 += 1
        return ugly


n = 9
n = 1
n = 2


solution = Solution()
print(solution.nth_ugly_number(n))
