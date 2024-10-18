class Solution:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimum_boxes(self, boxes, target):
        # write your code here
        # pre-process
        L = len(boxes)
        # construct presums
        presums = [0]
        for x in range(L):
            presums.append(presums[-1] + boxes[x])

        # process
        # find left_min
        # left_min[x] the min length of boxes[0:x] with sum of target
        left_min = [float("inf")] * (L + 1)
        left, right = 0, 1
        while right <= L:
            while left < right and presums[right] - presums[left] > target:
                left += 1
            if presums[right] - presums[left] == target:
                left_min[right] = right - left
            left_min[right] = min(left_min[right - 1], left_min[right])
            right += 1
        # print(left_min)

        # find right_min
        # right_min
        right_min = [float("inf")] * (L + 1)
        left, right = L - 1, L
        while left >= 0:
            while left < right and presums[right] - presums[left] > target:
                right -= 1
            if presums[right] - presums[left] == target:
                right_min[left] = right - left
            right_min[left] = min(right_min[left + 1], right_min[left])
            left -= 1
        # print(right_min)

        # stars and bars
        ans = float("inf")
        for x in range(0, L + 1):
            ans = min(ans, left_min[x] + right_min[x])
        return -1 if ans == float("inf") else ans


boxes = [1,2,2,1,1,1]
target = 3

#boxes = [1,1,2,2,1,1,2,2]
#target = 4

#boxes = []
#target = 1

solution = Solution()
print(solution.minimum_boxes(boxes, target))
