class Solution:
    """
    @param nums1: an integer array of length m with digits 0-9
    @param nums2: an integer array of length n with digits 0-9
    @param k: an integer and k <= m + n
    @return: an integer array
    """
    def select_n_from_nums(self, nums, n):
        if n == 0:
            return list()

        L = len(nums)
        stack = list()
        for idx, item in enumerate(nums):
            while len(stack) > 0 and stack[-1] < item and len(stack) + L - idx > n:
                stack.pop()
            stack.append(item)
        return stack[:n]

    def merge_two_nums(self, nums1, nums2):
        M = len(nums1)
        N = len(nums2)
        x = 0
        y = 0

        ans = ""
        while x < M and y < N:
            if nums1[x:] >= nums2[y:]:
                ans += str(nums1[x])
                x += 1
            else:
                ans += str(nums2[y])
                y += 1

        while x < M:
            ans += str(nums1[x])
            x += 1

        while y < N:
            ans += str(nums2[y])
            y += 1

        return int(ans)

    def max_number(self, nums1, nums2, k):
        # write your code here
        M = len(nums1)
        N = len(nums2)

        if M == 0 and N == 0 or k == 0:
            return []

        ans = 0
        for x in range(0, M + 1):
            y = k - x
            if 0 <= y <= N:
                selected1 = self.select_n_from_nums(nums1, x)
                selected2 = self.select_n_from_nums(nums2, y)
                merged_number = self.merge_two_nums(selected1, selected2)
                ans = max(ans, merged_number)

        return [int(_) for _ in str(ans)]


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5

nums1 = [3, 9]
nums2 = [8, 9]
k = 3

nums1 = []
nums2 = []
k = 0

nums1 = [1,6,5,4,7,3,9,5,3,7,8,4,1,1,4]
nums2 = [4,3,1,3,5,9]
k = 21

nums1 = [5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3]
nums2 = [7,6,7,1,0,1,0,5,6,0,5,0]
k = 31

nums1 = [3,3,1,8,2,4,2,9,2,4,7,1,9,2,3,4,0,7,5,4]
nums2 = [9,7,7,1,3,6,8,6,9,6,0,4,3,6,6,1,0,4,6,2,2,6,4,6,0,4,9,7,4,9,8,4,9,8,4,6,6,5,8,2,8,6,6,6,1,0,9,0,8,0,4,0,4,4,1,7,9,8,4,2,2,0,3,2,3,9,1,8,9,5,2,7,9,2,7,7,8,5,4,4,8,6,5,5,9,6,1,4,6,0,8,5,3,4,2,0,0,9,5,2]
k = 100

solution = Solution()
print(solution.max_number(nums1, nums2, k))
