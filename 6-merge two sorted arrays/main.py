class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a, b):
        # write your code here
        # pre-process
        A, B = len(a), len(b)
        idx, idx2 = 0, 0

        # process
        ans = list()
        while idx < A and idx2 < B:
            if a[idx] <= b[idx2]:
                ans.append(a[idx])
                idx += 1
            else:
                ans.append(b[idx2])
                idx2 += 1

        ans.extend(a[idx:])
        ans.extend(b[idx2:])
        return ans


a = [1,2,3,4]
b = [2,4,5,6]

solution = Solution()
print(solution.merge_sorted_array(a, b))
