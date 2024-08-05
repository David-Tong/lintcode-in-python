class Solution:
    """
    @param n: the n
    @return: the smallest lucky number  that is not less than n
    """
    def lucky_number(self, n):
        # Write your code here.
        length = len(n)
        half = length // 2
        if length % 2 == 1:
            half += 1
            return '3' * half + '5' * half
        if n > '5' * half + '3' * half:
            return '3' * (half + 1) + '5' * (half + 1)

        count3, count5 = half, half
        last3 = -1
        answer = ''
        for i in range(length):
            if count3 > 0 and n[i] <= '3':
                count3 -= 1
                answer += '3'
                last3 = i
                if n[i] < '3':
                    break
                else:
                    continue
            if count5 > 0 and n[i] <= '5':
                count5 -= 1
                answer += '5'
                if n[i] < '5':
                    break
                else:
                    continue
            while last3 < len(answer):
                if answer[-1] == '3':
                    count3 += 1
                else:
                    count5 += 1
                answer = answer[:-1]
            answer += '5'
            count5 -= 1
            break
        answer += '3' * count3 + '5' * count5

        return answer