class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k, nums):
        # write your code here
        def partition(low, high):
            pivot = nums[high]
            y = low
            for x in range(low, high):
                if nums[x] < pivot:
                    if x != y:
                        nums[x], nums[y] = nums[y], nums[x]
                    y += 1
            nums[high], nums[y] = nums[y], nums[high]
            return y

        def quick_sort(low, high):
            if low < high:
                pivot = partition(low, high)
                if pivot == L - k:
                    return nums[pivot]
                elif pivot > L - k:
                   return quick_sort(low, pivot - 1)
                else:
                    return quick_sort(pivot + 1, high)
            elif low == L - k:
                return nums[low]

        L = len(nums)
        return quick_sort(0, L - 1)


k = 1
nums = [1,3,4,2]

"""
k = 3
nums = [9,3,2,4,8]
"""

solution = Solution()
print(solution.kth_largest_element(k, nums))
