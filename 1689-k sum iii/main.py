class Solution:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    """
    def get_ans(self, a, k, target):
        # write your code here
        # pre-process
        odds = list()
        evens = list()
        for item in a:
            if item % 2 == 0:
                evens.append(item)
            else:
                odds.append(item)
        self.ans = 0

        def do_sum(arr, index, count, total):
            if count > k:
                return

            if index == len(arr):
                if count == k and total == target:
                    self.ans += 1
                return

            do_sum(arr, index + 1, count + 1, total + arr[index])
            do_sum(arr, index + 1, count, total)

        do_sum(odds, 0, 0, 0)
        do_sum(evens, 0, 0, 0)

        return self.ans


a = [1, 2, 3, 4]
k = 2
target = 4

a = [9, 1, 4, 4]
k = 3
target = 46
k = 2
target = 8

a = [3, 2, 3, 2, 1, 2, 4, 5, 4]
k = 2
target = 6

solution = Solution()
print(solution.get_ans(a, k, target))
