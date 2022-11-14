class Solution:
    """
    @param interval__a: a string represent a interval.
    @param interval__b: a string represent a interval.
    @return: if two intervals can merge return true, otherwise false.
    """
    def merge_judge(self, interval__a, interval__b):
        # write your code here
        # -1 - a < b, 0 - a == b, 1 - a > b
        def compare_string(a, b):
            L = min(len(a), len(b))
            idx = 0
            while idx < L:
                if a[idx] < b[idx]:
                    return -1
                elif a[idx] > b[idx]:
                    return 1
                idx += 1

            if len(a) > len(b):
                return 1
            elif len(a) < len(b):
                return -1
            else:
                return 0


        def contain_string(a, b):
            L = min(len(a), len(b))
            idx = 0
            while idx < L:
                if a[idx] == b[idx]:
                    idx += 1
                else:
                    return False
            return len(a) < len(b)

        def compare_operator(a, b):
            opers = {"[": 0, "(": 1, ")": 2, "]": 3}
            return opers[a] >= opers[b]

        # write your code here
        a = interval__a[1:-1].split(",")
        b = interval__b[1:-1].split(",")
        a_ops = [interval__a[0], interval__a[-1]]
        b_ops = [interval__b[0], interval__b[-1]]

        cmp = compare_string(a[0], b[0])
        if cmp > 0:
            (a, b) = (b, a)
            (a_ops, b_ops) = (b_ops, a_ops)
        elif cmp == 0:
            if compare_operator(a_ops[0], b_ops[1]):
                (a, b) = (b, a)
                (a_ops, b_ops) = (b_ops, a_ops)

        cmp = compare_string(a[1], b[0])
        if cmp == 1:
            return True
        elif cmp == 0:
            if b_ops[0] == "(" and a_ops[1] == ")":
                return False
            else:
                return True
        else:
            if contain_string(b[0], a[1]):
                return True
            elif contain_string(a[1], b[0]):
                if a_ops[1] == "]" and b_ops[0] == "[":
                    return True
            return False


interval__a = "[a,b]"
interval__b = "[b,c]"

interval__a = "[a,b]"
interval__b = "(b,c]"

interval__a = "[a,b)"
interval__b = "(b,c]"

interval__a = "(b,c)"
interval__b = "[a,b]"

interval__a = "(b,c)"
interval__b = "(a,b)"

interval__a = "(a,ab]"
interval__b = "[aba,c]"

"""
interval__a = "[abcdfaefasdczsrthwrtgapsodmc,abcdfaefasdczsrthwrtgapsodmd]"
interval__b = "[abcdfaefasdczsrthwrtgapsodm,abcdfaefasz]"

interval__a = "(b,ccccccccccccc)"
interval__b = "(aaaaaaaaaaa,bbbbbbbbbbbbbbbb)"

interval__a = "[a,asdfqwe)"
interval__b = "[asdfqwea,c]"

interval__a = "[a,asdfqwe]"
interval__b = "(asdfqwea,c]"
"""

solution = Solution()
print(solution.merge_judge(interval__a, interval__b))
