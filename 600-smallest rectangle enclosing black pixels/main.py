class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image, x, y):
        # write your code here
        M = len(image)
        N = len(image[0])

        rows = [False] * M
        lower = float("inf")
        upper = -1
        for idx, row in enumerate(image):
            for item in row:
                if item == "1":
                    rows[idx] = True
                    lower = min(lower, idx)
                    upper = max(upper, idx)
                    continue

        cols = [False] * N
        left = float("inf")
        right = -1
        for idx in range(N):
            for row in image:
                if row[idx] == "1":
                    cols[idx] = True
                    left = min(left, idx)
                    right = max(right, idx)
                    continue

        if x < lower:
            lower = x
        elif x > upper:
            upper = x

        if y < left:
            left = y
        elif y > right:
            right = y

        return (upper - lower + 1) * (right - left + 1)


image = ["0010","0110","0100"]
x = 0
y = 2

solution = Solution()
print(solution.min_area(image, x, y))