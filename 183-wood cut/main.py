class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l, k):
        # write your code here
        def can_cut(woods, k, length):
            n = 0
            for wood in woods:
                n += wood // length

            if n >= k:
                return True
            else:
                return False

        if len(l) == 0:
            return 0

        left = 1
        right = max(l)

        while left + 1 < right:
            middle = (left + right) // 2
            if can_cut(l, k, middle):
                left = middle
            else:
                right = middle - 1

        if can_cut(l, k, right):
            return right
        elif can_cut(l, k, left):
            return left
        else:
            return 0


l = [232, 124, 456]
k = 7

l = [1, 2, 3]
k = 7

l = []
k = 15

l = [1]
k = 12

solution = Solution()
print(solution.wood_cut(l, k))
