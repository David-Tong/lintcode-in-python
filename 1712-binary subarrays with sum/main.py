class Solution:
    """
    @param a: an array
    @param s: the sum
    @return: the number of non-empty subarrays
    """
    def num_subarrays_with_sum(self, a, s):
        # Write your code here.
        # pre-process
        from collections import defaultdict
        presums = defaultdict(int)
        presums[0] = 1
        presum = 0

        # process
        ans = 0
        for item in a:
            presum += item
            if presum - s in presums:
                ans += presums[presum - s]
            presums[presum] += 1
        return ans


A = [1,0,1,0,1]
S = 2

"""
A = [0,0,0,0,0,0,1,0,0,0]
S = 0
"""

solution = Solution()
print(solution.num_subarrays_with_sum(A, S))
