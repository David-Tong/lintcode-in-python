class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers):
        # write your code here
        L = len(numbers)
        numbers = sorted(numbers)

        anses = set()
        for idx, number in enumerate(numbers):
            left = idx + 1
            right = L - 1
            while left < right:
                if numbers[left] + numbers[right] < -1 * number:
                    left += 1
                elif numbers[left] + numbers[right] > -1 * number:
                    right -= 1
                else:
                    anses.add((number, numbers[left], numbers[right]))
                    left += 1
                    right -= 1

        return list(anses)


numbers = [2,7,11,15]
numbers = [-1,0,1,2,-1,-4]

solution = Solution()
print(solution.three_sum(numbers))
