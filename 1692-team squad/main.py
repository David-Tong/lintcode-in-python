class Solution:
    """
    @param atk1: the power of heros
    @param atk2: the power of monsters
    @return: how many monsters can you kill at most?
    """
    def get_ans(self, atk1, atk2):
        # Write your code here
        # pre-process
        N = len(atk1)
        atk1 = sorted(atk1)
        atk2 = sorted(atk2)

        idx1 = 0
        idx2 = 0
        killed = 0
        while idx1 < N:
            if atk1[idx1] > atk2[idx2]:
                killed += 1
                idx2 += 1
            idx1 += 1

        return killed


atk1 = [6, 4, 8, 5, 1]
atk2 = [2, 3, 4, 5, 6]

atk1 =[43,25,33,17]
atk2 = [41,41,17,11]

atk1 = [12, 2, 3, 6, 9, 15, 48]
atk2 = [11, 5, 6, 7, 100, 78, 12]

solution = Solution()
print(solution.get_ans(atk1, atk2))
