class Solution:
    """
    @param arr: the 01 array
    @param k: the limit
    @return: the sum of the interval
    """

    def interval_statistics(self, arr, k):
        # Write your code here.
        L = len(arr)

        presum = [0] * (L + 1)
        for x in range(L):
            presum[x + 1] = presum[x] + arr[x]

        from collections import defaultdict
        presum_dict = defaultdict(list)
        for idx, psm in enumerate(presum):
            presum_dict[psm].append(idx)

        for x in range(L):
            target = x - k


arr = [0, 0, 1, 0, 1, 1, 0]
k = 1

arr = [1, 1, 1, 0, 0, 1]
k = 2

arr = []
k = 2

solution = Solution()
print(solution.interval_statistics(arr, k))
