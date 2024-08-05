class Solution:
    """
    @param val: the personality value of user
    @return: Return their recommend friends' value
    """
    def get_ans(self, val):
        # Write your code here
        from bisect import bisect_left

        sort = list()
        ans = list()
        for idx, item in enumerate(val):
            if idx == 0:
                sort.append(item)
            else:
                idx_left = bisect_left(sort, item)
                if idx_left == 0:
                    friend = sort[idx_left]
                elif idx_left == len(sort):
                    friend = sort[idx_left - 1]
                else:
                    if item - sort[idx_left - 1] <= sort[idx_left] - item:
                        friend = sort[idx_left - 1]
                    else:
                        friend = sort[idx_left]
                sort.insert(idx_left, item)
                ans.append(friend)
        return ans


val = [8, 9, 7, 3, 0, 5, 11]
val = [465, 5464, 6467, 6466779, 6461, 56]

solution = Solution()
print(solution.get_ans(val))
