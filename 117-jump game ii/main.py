class Solution:
    """
    @param a: A list of integers
    @return: An integer
    """
    def jump(self, a):
        # write your code here
        L = len(a)
        if L <= 1:
            return 0

        # run greedy strategy
        limit = a[0]
        if limit >= L - 1:
            return 1

        jumps = 1
        for idx, item in enumerate(a):
            if idx > 0:
                if idx <= limit:
                    if limit < idx + a[idx]:
                        limit = idx + a[idx]
                        jumps += 1
                        if limit >= L - 1:
                            return jumps
                else:
                    return -1
        return jumps


A = [2,3,1,1,4]
A = [4,34]
#A = [2]
#A = [5,9,3,2,1,0,2,3,3,1,0,0]

solution = Solution()
print(solution.jump(A))
