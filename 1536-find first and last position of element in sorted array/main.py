class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def search_range(self, nums, target):
        # Write your code here.
        L = len(nums)

        # find first
        first = -1
        left = 0
        right = L - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1

            if nums[left] == target:
                first = left
            elif nums[right] == target:
                first = right

        # find last
        last = -1
        left = 0
        right = L - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle - 1

            if nums[right] == target:
                last = right
            elif nums[left] == target:
                last = left

        return [first, last]


nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

solution = Solution()
print(solution.search_range(nums, target))
