class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def max_area(self, heights):
        # write your code here
        L = len(heights)
        left = 0
        right = L - 1
        ans = 0
        while left < right:
            ans = max(ans, min(heights[left], heights[right]) * (right - left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return ans


heights = [1, 3, 2]
#heights = [1, 3, 2, 2]

solution = Solution()
print(solution.max_area(heights))
