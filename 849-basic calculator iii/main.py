class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        # Write your code here
        def find_matched_bracket(s, index):
            L = len(s)
            stack = list()
            for x in range(index, L):
                ch = s[x]
                if ch == "(":
                    stack.append(ch)
                elif ch == ")":
                    stack.pop()
                if len(stack) == 0:
                    return x

        def do_arithmetic(operator, operand, operand2):
            if operator == "+":
                return operand + operand2
            elif operator == "-":
                return operand - operand2
            elif operator == "*":
                return operand * operand2
            elif operator == "/":
                return operand / operand2

        def do_calculate(s):
            L = len(s)

            operators = list()
            operands = list()

            index = 0
            number = ""
            while index < L:
                ch = s[index]
                # parse number
                if ord("0") <= ord(ch) <= ord("9"):
                    number += ch
                else:
                    if len(number) > 0:
                        operands.append(int(number))
                        number = ""

                # parse operators and priorities
                if ch == "+" or ch == "-":
                    while operators:
                        operand2 = operands.pop()
                        operand = operands.pop()
                        operator = operators.pop()
                        result = do_arithmetic(operator, operand, operand2)
                        operands.append(result)
                    operators.append(ch)
                elif ch == "*" or ch == "/":
                    while operators and (operators[-1] == "*" or operators[-1] == "/"):
                        operand2 = operands.pop()
                        operand = operands.pop()
                        operator = operators.pop()
                        result = do_arithmetic(operator, operand, operand2)
                        operands.append(result)
                    operators.append(ch)
                elif ch == "(":
                    matched = find_matched_bracket(s, index)
                    result = do_calculate(s[index + 1: matched])
                    operands.append(result)
                    index = matched
                elif ch == ")":
                    pass
                elif ch == " ":
                    pass

                index += 1

            if len(number) > 0:
                operands.append(int(number))

            while operators:
                operand2 = operands.pop()
                operand = operands.pop()
                operator = operators.pop()
                result = do_arithmetic(operator, operand, operand2)
                operands.append(result)

            return operands[0]

        return do_calculate(s)


s = "1 + 1"
s = "6-4 / 2"
s = "6 - 4 / 2 / 2+ 2 + 5"
s = "6 - 4 / 2 +  6 / 3 + 2 / 1"
s = "6 - (4 + 2)"
s = "6 / 2 + (2 + 3) + 3 / 3 + 1 + ((2 + 2) + 2) "

solution = Solution()
print(solution.calculate(s))
