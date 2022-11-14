class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binary_representation(self, n):
        # write your code here
        ns = n.split(".")
        integer = int(ns[0])
        if len(ns) > 1:
            decimal = float("0." + ns[1])

        integer_binary = list()
        while integer:
            integer_binary.append(str(integer % 2))
            integer = integer // 2

        decimal_binary = list()
        if len(ns) > 1:
            while abs(decimal - 0) > 1e-32:
                if decimal * 2 - 1 >= 0:
                    decimal_binary.append("1")
                    decimal = decimal * 2 - 1
                else:
                    decimal_binary.append("0")
                    decimal = decimal * 2

                if len(decimal_binary) > 32:
                    return "ERROR"

        if len(decimal_binary):
            if len(integer_binary):
                return "".join(integer_binary[::-1]) + "." + "".join(decimal_binary)
            else:
                return "0." + "".join(decimal_binary)
        else:
            if len(integer_binary):
                return "".join(integer_binary[::-1])
            else:
                return "0"


n = "3.4999999999"
n = "0.5"
n = "0.0"
n = "6.125"
n = "17817287.6418609619140625"
n = "0"
n = "9"

solution = Solution()
print(solution.binary_representation(n))
