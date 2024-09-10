class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums, k):
        # write your code here
        # pre-process
        from collections import defaultdict
        dicts = defaultdict(list)
        dicts[0].append(0)

        # process
        presum = 0
        ans = float("inf")
        for idx, num in enumerate(nums):
            presum += num
            target = presum - k
            if target in dicts:
                ans = min(ans, idx + 1 - dicts[target][-1])
            dicts[presum].append(idx + 1)

        # print(dicts)
        return -1 if ans == float("inf") else ans


nums = [1,1,1,2]
k = 3

nums = [2,1,-1,4,2,-3]
k = 3

solution = Solution()
print(solution.subarray_sum_equals_k_i_i(nums, k))
