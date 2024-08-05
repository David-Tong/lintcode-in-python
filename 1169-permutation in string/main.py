class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def check_inclusion(self, s1, s2):
        # write your code here
        # pre-process
        M = len(s1)
        N = len(s2)
        from collections import defaultdict
        dicts = defaultdict(int)
        for ch in s1:
            dicts[ch] += 1

        # process
        left = 0
        right = 0
        while right < N:
            if s2[right] in dicts:
                dicts[s2[right]] -= 1

            while right - left > M - 1:
                if s2[left] in dicts:
                    dicts[s2[left]] += 1
                left += 1

            if right - left == M - 1:
                if sum(dicts.values()) == 0:
                    return True
            right += 1
        return False


s1 = "ab"
s2 = "eidbaooo"

s1= "ab"
s2 = "eidboaoo"

s1 = "aac"
s2 = "ryiffcacef"

solution = Solution()
print(solution.check_inclusion(s1, s2))
