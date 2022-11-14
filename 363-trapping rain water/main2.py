class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights):
        # write your code here
        L = len(heights)
        rights = [0] * L
        max_right = 0
        for x in range(L - 1, -1, -1):
            rights[x] = max(max_right, heights[x])
            max_right = max(max_right, heights[x])

        lefts = [0] * L
        max_left = 0
        for x in range(L):
            lefts[x] = max(max_left, heights[x])
            max_left = max(max_left, heights[x])

        ans = 0
        for x in range(L):
            ans += max(0, min(lefts[x], rights[x]) - heights[x])
        return ans


heights = [0,1,0]
#heights = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap_rain_water(heights))
