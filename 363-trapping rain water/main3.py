class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights):
        # write your code here
        L = len(heights)
        if L == 0:
            return 0

        left = 0
        right = L - 1
        max_left, max_right = heights[left], heights[right]
        ans = 0
        while left < right:
            max_left = max(max_left, heights[left])
            max_right = max(max_right, heights[right])
            if heights[left] < heights[right]:
                ans += max(0, min(max_left, max_right) - heights[left])
                left += 1
            else:
                ans += max(0, min(max_left, max_right) - heights[right])
                right -= 1
        return ans


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
heights = [0,1,0]
heights = [1]
#heights = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap_rain_water(heights))
