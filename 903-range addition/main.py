class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def get_modified_array(self, length, updates):
        # Write your code here
        # pre-process
        diffs = [0] * length

        for update in updates:
            start, end, inc = update
            diffs[start] += inc
            if end + 1 < length:
                diffs[end + 1] -= inc

        # process
        nums = [0] * length
        for x in range(length):
            if x == 0:
                nums[x] = diffs[x]
            else:
                nums[x] = nums[x - 1] + diffs[x]
        return nums


length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]

solution = Solution()
print(solution.get_modified_array(length, updates))
