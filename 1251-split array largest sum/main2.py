class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def split_array(self, nums, m):
        # write your code here
        def can_split(nums, m, k):
            N = len(nums)
            total = 0
            splits = 1
            for x in range(N):
                if nums[x] > k:
                    return False

                if total + nums[x] <= k:
                    total += nums[x]
                else:
                    total = nums[x]
                    splits += 1
                    if splits > m:
                        return False

                # check if remaining elements in the array is equal to the remaining to split number
                remaining_elements = N - 1 - x
                remaining_splits = m - splits
                if remaining_elements == remaining_splits:
                    break
                elif remaining_elements < remaining_splits:
                    return False

            for y in range(x, N):
                if nums[y] > k:
                    return False
            return True

        left = 0
        right = sum(nums)
        while left + 1 < right:
            middle = (left + right) // 2
            if can_split(nums, m, middle):
                # print("can split with k : " + str(middle))
                right = middle - 1
            else:
                # print("can't split with k : " + str(middle))
                left = middle + 1

        if can_split(nums, m, left):
            return left
        elif can_split(nums, m, right):
            return right
        else:
            return right + 1


nums = [7, 2, 5, 10, 8]
m = 2

nums = [1, 4, 4]
m = 3

nums = [6, 2, 0, 0, 2]
m = 4

solution = Solution()
print(solution.split_array(nums, m))