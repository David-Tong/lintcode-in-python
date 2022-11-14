class Solution:
    """
    @param nums: an array of integers
    @param threshold: an integer
    @return: return the smallest divisor
    """
    def smallest_divisor(self, nums, threshold):
        # write your code here
        def is_valid(nums, threshold, divisor):
            from math import ceil
            total = 0
            for num in nums:
                total += ceil(num * 1.0 / divisor)
            if total <= threshold:
                return True
            else:
                return False

        left = 1
        right = max(nums)

        while left + 1 < right:
            middle = (left + right) // 2
            if is_valid(nums, threshold, middle):
                right = middle
            else:
                left = middle + 1

        if is_valid(nums, threshold, left):
            return left
        else:
            return right


nums = [1,2,5,9]
threshold = 6

nums = [2,3,5,7,11]
threshold = 11

nums = [19]
threshold = 5

solution = Solution()
print(solution.smallest_divisor(nums, threshold))
