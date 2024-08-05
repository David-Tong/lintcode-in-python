class Solution:
    """
    @param a: the n numbers
    @param k: the number of integers you can choose
    @return: how many ways that the sum of the k integers is a prime number
    """

    def get_ways(self, a, k):
        # Write your code here
        def isPrime(target):
            lower = 2
            upper = target // 2 + 1
            for x in range(lower, upper):
                if target % x == 0:
                    return False
            return True

        L = len(a)
        self.ans = 0

        def do_ways(idx, count, selected):
            if count == k:
                target = sum(selected)
                if isPrime(target):
                    self.ans += 1
                return

            if idx < L:
                do_ways(idx + 1, count + 1, selected + [a[idx]])
                do_ways(idx + 1, count, selected)

        do_ways(0, 0, list())
        return self.ans


a = [1,2,3]
k = 2

a = []
k = 3

solution = Solution()
print(solution.get_ways(a, k))
