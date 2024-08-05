class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def length_of_last_word(self, s):
        # write your code here
        L = len(s)
        idx = L - 1
        end = L

        # filter our space in the end
        while idx >=0 and s[idx] == ' ':
            idx -= 1
            end -= 1

        # calculate the lasdt work length
        while idx >= 0 and s[idx] != ' ':
            idx -= 1
        return end - idx - 1


s = "Hello World"
s = "Hello LintCode"
s = "Hello  "
s = "  "
s = ""

solution = Solution()
print(solution.length_of_last_word(s))
