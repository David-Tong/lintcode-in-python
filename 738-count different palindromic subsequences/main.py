class Solution:
    """
    @param str: a string S
    @return: the number of different non-empty palindromic subsequences in S
    """
    def count_palind_subseq(self, s):
        # write your code here
        def count(start, end):
            # base case 1
            # when x is empty
            if start > end:
                return 0
            # base case 2
            # when x in "a", "b", "c", "d"
            elif start == end:
                return 1

            # search cache
            key = str(start) + "-" + str(end)
            if key in cache:
                return cache[key]

            # when str[start] == str[end]
            if s[start] == s[end]:
                left = start + 1
                right = end - 1
                while left <= right and s[left] != s[start]:
                    left += 1
                while left <= right and s[right] != s[end]:
                    right -= 1
                if left > right:
                    # case 1 : doesn't include s[start] in s[start + 1: end]
                    # count("bccb") = 2 * count("cc") + 2 : "c", "cc", "bcb", "bccb", "b", "bb"
                    # count("cc") = 2 * count("") + 2 : "c", "cc"
                    ans = 2 * count(start + 1, end - 1) + 2
                elif left == right:
                    # case 3 : include s[start] in s[start + 1: end] for once
                    # count("bcbcb") = 2 * count("cbd") + 1 : "b", "cbc", "cc", "c", "bbb", "bcbcb", "bccb", "bcb", "bb"
                    # count("cbc") = 2 * count("b") + 2 : "b", "cbc", "cc", "c"
                    ans = 2 * count(start + 1, end - 1) + 1
                else:
                    # case 4 : include s[start] in s[start + 1: end] for twice
                    # count("bbcabb") = 2 * count("bcab") - count("ca") :
                    # "c", "a", "bcb", "bab", "b", "bb", "bcb”, "bab", "bbcbb", "bbabb", "bbb", "bb" - "bcb", "bab"
                    # count("bcab") = 2 * count("ca") + 2 : "c", "a", "bcb", "bab", "b", "bb"
                    ans = 2 * count(start + 1, end - 1) - count(left + 1, right - 1)
            else:
                # case 2
                # count("abccb") = count("abcc") + count("bccb") - count("bcc")
                # where "bcc" is counted for twice
                ans = count(start, end - 1) + count(start + 1, end) - count(start + 1, end - 1)

            cache[key] = ans
            return ans

        MODULO = 10 ** 9 + 7
        L = len(s)
        from collections import defaultdict
        cache = defaultdict(long)
        return count(0, L - 1) % MODULO


s = "bccb"
s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"

solution = Solution()
print(solution.count_palind_subseq(s))
