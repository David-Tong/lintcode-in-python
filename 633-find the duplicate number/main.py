class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def find_duplicate(self, nums):
        # write your code here
        # find the joint point
        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        slow = 0
        slow = nums[slow]
        fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [5,5,4,3,2,1]
nums = [5,4,4,3,2,1]

solution = Solution()
print(solution.find_duplicate(nums))
