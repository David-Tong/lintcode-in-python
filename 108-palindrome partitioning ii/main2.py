class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def min_cut(self, s):
        # write your code here
        # pre-process
        L = len(s)

        # is palindrome
        palindromes = [[True] * L for _ in range(L)]
        for x in range(L - 1, -1, -1):
            for y in range(x + 1, L):
                palindromes[x][y] = palindromes[x + 1][y - 1] and s[x] == s[y]

        # do min cut for s[x:]
        def do_min_cut(start):
            if start in cache:
                return cache[start]
            if palindromes[start][L - 1]:
                return 0
            min_cut = float("inf")
            for x in range(start, L):
                if palindromes[start][x]:
                    min_cut = min(min_cut, do_min_cut(x + 1) + 1)
            cache[start] = min_cut
            cache[start] = min_cut
            return min_cut

        from collections import defaultdict
        cache = defaultdict(int)
        return do_min_cut(0)


s = "a"
s = "aab"
s = "abacabac"
s = "sfsdkjgfuiwbfkwfbvkjfneiwhehfeifhfiefwhihifhhhhhhhhhhhhhhhhhhhhhhhhefwjhweg"

solution = Solution()
print(solution.min_cut(s))