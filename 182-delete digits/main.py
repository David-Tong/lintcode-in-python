class Solution:
    """
    @param a: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def delete_digits(self, a, k):
        # write your code here
        # process
        stack = list()
        c = 0
        for d in a:
            while stack and stack[-1] > d:
                if c < k:
                    stack.pop()
                    c += 1
                else:
                    break
            stack.append(d)

        # post-process
        ans = "".join(stack)
        if c < k:
            ans = ans[:c - k]
        ans = str(int(ans))
        return ans


A = "178542"
k = 4

A = "568431"
k = 3

A = "98493729892385912"
k = 7

A = "90249"
k = 2

solution = Solution()
print(solution.delete_digits(A, k))
