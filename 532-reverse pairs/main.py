class Solution:
    """
    @param a: an array
    @return: total of reverse pairs
    """
    def reverse_pairs(self, a):
        # write your code here
        self.ans = 0

        def partition(a):
            L = len(a)
            if L == 1:
                return a
            else:
                idx = L // 2
                a1 = partition(a[:idx])
                a2 = partition(a[idx:])
                return merge(a1, a2)

        def merge(a1, a2):
            idx1 = 0
            idx2 = 0
            M = len(a1)
            N = len(a2)

            a = list()
            while idx1 < M and idx2 < N:
                if a1[idx1] <= a2[idx2]:
                    a.append(a1[idx1])
                    idx1 += 1
                else:
                    a.append(a2[idx2])
                    idx2 += 1
                    self.ans += M - idx1

            while idx1 < M:
                a.append(a1[idx1])
                idx1 += 1

            while idx2 < N:
                a.append(a2[idx2])
                idx2 += 1

            return a

        if len(a) == 0:
            return 0

        partition(a)
        return self.ans


a = [2, 4, 1, 3, 5]
a = [1, 2, 3, 4]

a = [4, 3, 2, 1]
a = [1]

solution = Solution()
print(solution.reverse_pairs(a))
