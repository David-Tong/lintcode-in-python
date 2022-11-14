class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def cal_points(self, ops):
        # Write your code here
        stack = list()
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)


ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]

solution = Solution()
print(solution.cal_points(ops))
