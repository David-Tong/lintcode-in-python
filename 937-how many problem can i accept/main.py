class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """
    def can_accept(self, n, k):
        # Write your code here
        def add_up(i, k):
            return k * i * (i + 1) // 2

        left = 0
        right = n
        while left + 1 < right:
            middle = (left + right) // 2
            total = add_up(middle, k)
            if total < n:
                left = middle + 1
            elif total > n:
                right = middle - 1
            else:
                return middle

        if add_up(right, k) <= n:
            return right
        elif add_up(left, k) <= n:
            return left
        else:
            return left - 1


n = 30
k = 1

n = 31
k = 2

n = 1
k = 2

solution = Solution()
print(solution.can_accept(n, k))
