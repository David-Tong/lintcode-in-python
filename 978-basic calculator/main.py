class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        # pre-process
        if s[0] == "-":
            s = "0" + s
        for idx, ch in enumerate(s):
            if ch == "(" and s[idx + 1] == "-":
                s = s[:idx + 1] + "0" + s[idx + 1:]
        L = len(s)
        # print(s)

        # process
        from collections import deque
        stack = list()
        pre = -1
        for idx, ch in enumerate(s):
            if ch in ["+", "-", " ", "(", ")"]:
                if pre != -1:
                    stack.append(int(s[pre:idx]))
                    pre = -1
                if ch in ["+", "-", "("]:
                    stack.append(ch)
                elif ch in [")"]:
                    queue = deque()
                    while stack[-1] != "(":
                        queue.appendleft(stack.pop())
                    stack.pop()
                    while len(queue) > 1:
                        operand = queue.popleft()
                        operator = queue.popleft()
                        operand2 = queue.popleft()
                        if operator == "+":
                            queue.appendleft(operand + operand2)
                        elif operator == "-":
                            queue.appendleft(operand - operand2)
                    stack.append(queue[0])
            else:
                if pre == -1:
                    pre = idx

        if pre != -1:
            stack.append(int(s[pre:L]))

        queue = deque()
        while stack:
            queue.appendleft(stack.pop())
        while len(queue) > 1:
            operand = queue.popleft()
            operator = queue.popleft()
            operand2 = queue.popleft()
            if operator == "+":
                queue.appendleft(operand + operand2)
            elif operator == "-":
                queue.appendleft(operand - operand2)

        ans = queue[0]
        return ans


s = "1 + 1"
s = "(1+(4+5+2)-3)+(6+8)"
s = "-6+(-1+(4+5+2)-3)+(6+8)"
s = "-6 +(-1 +(4+5 +2)-3)+(6 + 8)"
s = "0-6+(0-1+(4+5+2)-3)+(6+8)"


solution = Solution()
print(solution.calculate(s))
