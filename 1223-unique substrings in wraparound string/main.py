class Solution:
    """
    @param p: the given string
    @return: the number of different non-empty substrings of p in the string s
    """
    def find_substring_in_wrapround_string(self, p):
        # Write your code here
        # pre-process
        if not p: return 0
        L = len(p)

        from collections import defaultdict
        dicts = defaultdict(int)

        seq = 1
        for x in range(L):
            if x > 0:
                if p[x] == 'a' and p[x - 1] == 'z' or p[x - 1] == chr(ord(p[x]) - 1):
                    seq += 1
                else:
                    for y in range(x - seq, x):
                        dicts[p[y]] = max(dicts[p[y]], x - y)
                    seq = 1

        for y in range(L - seq, L):
            dicts[p[y]] = max(dicts[p[y]], L - y)
        # print(dicts)

        # process
        ans = sum(dicts.values())
        return ans


p = "a"
p = "ab"
p = "ac"
p = "cac"
p = "zab"
p = "zababcef"
p = "abcab"
p = ""

solution = Solution()
print(solution.find_substring_in_wrapround_string(p))
