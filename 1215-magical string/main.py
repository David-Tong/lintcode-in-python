class Solution:
    """
    @param n: an integer
    @return: the number of '1's in the first N number in the magical string S
    """
    def magical_string(self, n):
        # write your code here
        # p1 - point to string, p2 - point to occurrences
        p1, p2 = 0, 0
        magic = "1"

        while len(magic) <= n:
            if p1 == p2:
                if magic[p1] == "1":
                    magic += "22"
                    p1 += 2
                    p2 += 1
                else:
                    magic += "1"
                    p1 += 1
                    p2 += 1
            elif p2 < p1:
                if magic[p1] == "1":
                    magic += "2" * int(magic[p2 + 1])
                else:
                    magic += "1" * int(magic[p2 + 1])
                p1 += int(magic[p2 + 1])
                p2 += 1

        ans = 0
        for x in range(n):
            if magic[x] == "1":
                ans += 1
        return ans


n = 6
n = 3

solution = Solution()
print(solution.magical_string(n))
