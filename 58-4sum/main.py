class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """
    def four_sum(self, numbers, target):
        # write your code here
        L = len(numbers)
        numbers = sorted(numbers)

        anses = set()
        for idx in range(L):
            for idx2 in range(idx + 1, L):
                left = idx2 + 1
                right = L - 1
                while left < right:
                    total = numbers[idx] + numbers[idx2] + numbers[left] + numbers[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans = (numbers[idx], numbers[idx2], numbers[left], numbers[right])
                        anses.add(ans)
                        right -= 1
                        left += 1
        return anses


numbers = [2,7,11,15]
target = 3

numbers = [1,0,-1,0,-2,2]
target = 0

numbers = [1,0,-1,-1,-1,-1,0,1,1,1,2]
target = 2

solution = Solution()
print(solution.four_sum(numbers, target))
