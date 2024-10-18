class Solution:
    """
    @param boxes: List[int]
    @return: return an integer
    """
    def remove_boxes(self, boxes):
        # write your code here
        L = len(boxes)
        cache = [[[0] * L for _ in range(L)] for _ in range(L)]

        def dfs(l, r, k):
            if l > r:
                return 0

            if cache[l][r][k] != 0:
                return cache[l][r][k]

            # example
            # ... OOO XXX OOO XXX OOO
            #       ^   ^   ^   ^   ^
            #       j1  i1  j0  i0  r

            # merge all tailing boxes with the same color
            # i - the position of i0
            i = r
            count = k
            while i >= l and boxes[i] == boxes[r]:
                i -= 1
                count += 1
            cache[l][r][k] = dfs(l, i, 0) + count * count

            # search for all possible connections, for j1, j0, get the max one
            j = i
            while j >= l:
                if boxes[j] != boxes[r]:
                    j -= 1
                    continue
                if boxes[j] == boxes[r] and boxes[j + 1] == boxes[r]:
                    j -= 1
                    continue
                cache[l][r][k] = max(cache[l][r][k], dfs(l, j, count) + dfs(j + 1, i, 0))
                j -= 1

            return cache[l][r][k]

        return dfs(0, L - 1, 0)


boxes = [1, 3, 1]
boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
boxes = [1,2,3,4,5,6,7,8,9,10]

solution = Solution()
print(solution.remove_boxes(boxes))
