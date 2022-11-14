class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        if id >= 1:
            return True
        else:
            return False

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        left = 1
        right = n

        while left + 1 < right:
            middle = (left + right) // 2
            bad = SVNRepo.isBadVersion(middle)
            if bad:
                right = middle - 1
            else:
                left = middle + 1


        if SVNRepo.isBadVersion(left):
            return left
        elif SVNRepo.isBadVersion(right):
            return right
        else:
            return right + 1


n = 5

solution = Solution()
print(solution.findFirstBadVersion(n))
