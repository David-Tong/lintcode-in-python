class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums):
        # Write your code here
        L = len(nums)

        left = -1
        right = 0
        ans = 0
        while right < L:
            if nums[right] == 1:
                if left == -1:
                    left = right
            else:
                if left != -1:
                    ans = max(ans, right - left)
                    left = -1
            right += 1

        if left != -1:
            ans = max(ans, right - left)

        return ans


nums = [1,1,0,1,1,1]
nums = [1]
nums = [0,0,1,1,0,0,0,1,1,1,1]

solution = Solution()
print(solution.find_max_consecutive_ones(nums))
