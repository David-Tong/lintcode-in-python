class Solution:
    """
    @param arr: the 01 array
    @param k: the limit
    @return: the sum of the interval
    """
    def interval_statistics(self, arr, k):
        # Write your code here.
        L = len(arr)

        left = 0
        right = 0
        ones = 0
        ans = 0
        while right < L:
            if arr[right] == 1:
                ones += 1

            while ones > k:
                if arr[left] == 1:
                    ones -= 1
                left += 1

            if arr[right] == 0:
                zeros = right - left + 1 - ones
                ans += zeros
            right += 1

        return ans


arr = [0, 0, 1, 0, 1, 1, 0]
k = 1

arr = [1, 1, 1, 0, 0, 1]
k = 2

solution = Solution()
print(solution.interval_statistics(arr, k))


