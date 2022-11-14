class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def k_empty_slots(self, flowers, k):
        # Write your code here
        L = len(flowers)
        if L <= 1 or k >= L:
            return -1

        BS = (L + k) / (k + 1)
        lows = [float("inf")] * BS
        highs = [float("-inf")] * BS

        for x in range(L):
            idx = flowers[x] - 1
            bucket = idx / (k + 1)
            if idx < lows[bucket]:
                lows[bucket] = idx
                if bucket > 0 and highs[bucket - 1] == idx - k - 1:
                    return x + 1
            if idx > highs[bucket]:
                highs[bucket] = idx
                if bucket < BS - 1 and lows[bucket + 1] == idx + k + 1:
                    return x + 1
        return -1


flowers = [1,2,3,4]
k = 1

flowers = [1,3,2]
k = 1

flowers = [1,5,3,2,4]
k = 2

flowers = [10,1,9,3,5,7,6,4,8,2]
k = 8

flowers = [6,5,8,9,7,1,10,2,3,4]
k = 2

solution = Solution()
print(solution.k_empty_slots(flowers, k))