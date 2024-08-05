class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """

    def k_sum_i_i(self, a, k, target):
        # write your code here
        L = len(a)
        self.ans = list()

        def do_sum(index, count, total, selected):
            if count == k:
                if total == target:
                    from copy import deepcopy
                    self.ans.append(deepcopy(selected))
                    return
            if index < L:
                if total + a[index] <= target:
                    do_sum(index + 1, count + 1, total + a[index], selected + [a[index]])

                if total <= target:
                    do_sum(index + 1, count, total, selected)

        do_sum(0, 0, 0, list())
        return self.ans


array = [1, 2, 3, 4]
k = 2
target = 5

array = [1,3,4,6]
k = 3
target = 8

array = [1,1,1,1,1]
k = 3
target = 3

solution = Solution()
print(solution.k_sum_i_i(array, k, target))
