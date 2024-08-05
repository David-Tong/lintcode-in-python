class Solution:
    """
    @param a:
    @return:
    """
    def play_games(self, a):
        # Write your code here
        def can_play(target):
            if target < max(a):
                return False

            total = 0
            for item in a:
                # time every player can to be referee
                total += (target - item)
            if total >= target:
                return True
            else:
                return False

        left = min(a)
        right = min(a) + max(a)
        while left + 1 < right:
            middle = (left + right) // 2
            if can_play(middle):
                right = middle
            else:
                left = middle + 1

        if can_play(left):
            return left
        else:
            return right


A = [2, 2, 2, 2]
#A = [84, 53]
#A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#A = [1, 2, 3, 4, 5]

solution = Solution()
print(solution.play_games(A))
