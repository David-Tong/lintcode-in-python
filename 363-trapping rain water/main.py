class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trap_rain_water(self, heights):
        # write your code here
        L = len(heights)
        stack = list()
        rights = [0] * L
        for idx in range(L - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] < heights[idx]:
                rights[stack[-1]] = heights[stack[0]]
                stack.pop()
            stack.append(idx)

        while len(stack) > 0:
            rights[stack[-1]] = heights[stack[0]]
            stack.pop()

        stack = list()
        lefts = [0] * L
        for idx in range(L):
            while len(stack) > 0 and heights[stack[-1]] < heights[idx]:
                lefts[stack[-1]] = heights[stack[0]]
                stack.pop()
            stack.append(idx)

        while len(stack) > 0:
            lefts[stack[-1]] = heights[stack[0]]
            stack.pop()

        ans = 0
        for x in range(L):
            ans += max(0, min(lefts[x], rights[x]) - heights[x])
        return ans


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
heights = [0,1,0]
heights = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
print(solution.trap_rain_water(heights))
