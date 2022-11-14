class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def length_of_longest_substring(self, s):
        # write your code here
        L = len(s)
        from collections import defaultdict
        dicts = defaultdict(int)

        left = 0
        right = 0
        ans = 0
        while right < L:
            dicts[s[right]] += 1

            while dicts[s[right]] > 1:
                dicts[s[left]] -= 1
                left += 1

            right += 1
            ans = max(ans, right - left)
        return ans


s = "abcabcbb"
s = "bbbbb"
s = ""

solution = Solution()
print(solution.length_of_longest_substring(s))
