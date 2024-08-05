class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """

    def reach_number(self, target):
        # Write your code here
        target = abs(target)

        def search_number(search):
            if search * (search + 1) // 2 >= target:
                return True
            else:
                return False

        left = 0
        right = 10 ** 9

        while left + 1 < right:
            middle = (left + right) // 2
            if search_number(middle):
                right = middle
            else:
                left = middle + 1

        if search_number(left):
            start = left
        else:
            start = right

        while target % 2 != (start * (start + 1) // 2) % 2:
            start += 1
        return start

target = 0
target = 3
target = 2
target = 1000
target = -3

solution = Solution()
print(solution.reach_number(target))
