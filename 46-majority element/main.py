class Solution:
    """
    @param nums: a list of integers
    @return: find a  majority number
    """
    def majority_number(self, nums):
        # write your code here
        majority = ""
        count = 0
        for num in nums:
            if num == majority:
                count += 1
                if majority == "":
                    majority = num
            else:
                if majority == "":
                    majority = num
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        majority = ""
        return majority


nums = [1, 1, 1, 1, 2, 2, 2]
nums = [1, 1, 1, 2, 2, 2, 2]
nums = [1, 1, 2, 3, 2, 3, 3, 3, 3]

solution = Solution()
print(solution.majority_number(nums))
