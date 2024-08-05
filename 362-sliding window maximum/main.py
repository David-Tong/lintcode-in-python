class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def max_sliding_window(self, nums, k):
        # write your code here
        # shortcut
        L = len(nums)
        if L == 0 or k == 0 or L < k:
            return list()

        # pre-process
        from collections import deque
        queue = deque()
        for x in range(k):
            while queue and queue[-1] < nums[x]:
                queue.pop()
            queue.append(nums[x])

        # process
        ans = list()
        for x in range(L - k):
            ans.append(queue[0])
            if nums[x] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[x + k]:
                queue.pop()
            queue.append(nums[x + k])
        ans.append(queue[0])
        return ans


nums = [1,2,7,7,8]
k = 3

nums = [1,2,3,1,2,3]
k = 5

nums = [2,3,4,5,6,7,1,2,3,4,5,6,9]
k = 2

nums = []
k = 0

nums = [1]
k = 1

nums = [1]
k = 2

solution = Solution()
print(solution.max_sliding_window(nums, k))
