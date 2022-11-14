class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a):
        # write your code here
        if len(a) == 0:
            return 0

        signal = ""
        ans = 0
        for idx, num in enumerate(a):
            if idx == 0:
                curr = num
                start = idx
            else:
                prev = curr
                curr = num
                delta = curr - prev
                if delta > 0:
                    if signal == "-":
                        ans = max(ans, idx - start)
                        start = idx - 1
                        signal = "+"
                    elif signal == "":
                        signal = "+"
                elif delta < 0:
                    if signal == "+":
                        ans = max(ans, idx - start)
                        start = idx - 1
                        signal = "-"
                    elif signal == "":
                        signal = "-"
        ans = max(ans, idx - start + 1)
        return ans


a = [5, 4, 2, 1, 3]
a = [5, 4, 2, 1, 0]
a = [5, 1, 2, 3, 4]
a = [1, 2, 3, 4, 5]
a = [2, 2, 2, 2, 2]
a = [2, 2, 3, 3, 2, 1]

solution = Solution()
print(solution.longest_increasing_continuous_subsequence(a))
