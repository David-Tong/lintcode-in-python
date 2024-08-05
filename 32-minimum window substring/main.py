class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def min_window(self, source, target):
        # write your code here
        # pre-process
        L = len(source)

        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in target:
            dicts[ch] += 1

        # process
        def check(dicts):
            for key in dicts:
                if dicts[key] > 0:
                    return False
            return True

        left = 0
        right = 0
        mini = float("inf")
        ans = ""
        while right < L:
            # add
            if source[right] in dicts:
                dicts[source[right]] -= 1
            right += 1

            # reduce
            while check(dicts):
                if right - left < mini:
                    mini = right - left
                    ans = source[left:right]
                if source[left] in dicts:
                    dicts[source[left]] += 1
                left += 1

        return ans


source = "abc"
target = "ac"

source = "adobecodebanc"
target = "abc"

source = "abc"
target = "aa"

source = "aabcb"
target = "ac"

solution = Solution()
print(solution.min_window(source, target))
