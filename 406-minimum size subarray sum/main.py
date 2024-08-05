class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimum_size(self, nums, s):
        # write your code here
        L = len(nums)
        left = 0
        right = 0
        # sliding window
        total = 0
        ans = float("inf")
        while right < L:
            total += nums[right]
            right += 1
            while total >= s:
                ans = min(ans, right - left)
                total -= nums[left]
                left += 1
        return -1 if ans == float("inf") else ans


nums = [2,3,1,2,4,3]
s = 7

nums = [1,2,3,4,5]
s = 100

solution = Solution()
print(solution.minimum_size(nums, s))
