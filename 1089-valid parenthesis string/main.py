class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def check_valid_string(self, s):
        # Write your code here
        # pre-process
        lefts = list()
        stars = list()

        # match ')'
        for idx, ch in enumerate(s):
            if ch == '(':
                lefts.append(idx)
            elif ch == '*':
                stars.append(idx)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        # match '('
        idx_left, idx_star = 0, 0
        while idx_left < len(lefts) and idx_star < len(stars):
            if lefts[idx_left] < stars[idx_star]:
                idx_left += 1
            idx_star += 1

        if idx_left < len(lefts):
            return False

        return True


s = "()"
s = "(*)"
s = "(*))"
s = "((*(())**"
s = "*(()"

solution = Solution()
print(solution.check_valid_string(s))
