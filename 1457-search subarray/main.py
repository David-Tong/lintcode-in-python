class Solution:
    """
    @param arr: The array
    @param k: the sum
    @return: The length of the array
    """
    def search_subarray(self, arr, k):
        # Write your code here
        from collections import defaultdict
        prefixes = defaultdict(list)
        prefixes[0].append(0)

        prefix = 0
        for idx, item in enumerate(arr):
            prefix += item
            target = prefix - k
            if target in prefixes:
                return idx - prefixes[target][0] + 1
            prefixes[prefix].append(idx + 1)
        return -1


arr = [1,2,3,4,5]
k = 5

arr = [3,5,7,10,2]
k = 12

arr = [1,-1,0]
k = 0

solution = Solution()
print(solution.search_subarray(arr, k))