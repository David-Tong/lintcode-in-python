class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        self.anses = list()

        def is_partition(s):
            L = len(s)
            if L == 1:
                return True

            if L % 2 == 0:
                left = L // 2 - 1
                right = L // 2
            else:
                left = L // 2
                right = L // 2

            while left >= 0:
                if s[left] != s[right]:
                    return False
                left -= 1
                right += 1

            return True

        def do_partition(s, partitions):
            L = len(s)
            if L == 0:
                self.anses.append(partitions)

            for x in range(1, L + 1):
                if is_partition(s[:x]):
                    do_partition(s[x:], partitions + [s[:x]])

        do_partition(s, list())
        return self.anses


s = "a"
s = "aab"
s = ""

solution = Solution()
print(solution.partition(s))
