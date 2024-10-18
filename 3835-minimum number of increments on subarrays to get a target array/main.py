class Solution:
    """
    @param target: An integer array
    @return: The number of operations needed to get from initial to target array
    """
    def min_number_operation(self, target):
        # write your code here
        target.append(0)
        stack = list()
        ans = 0
        for item in target:
            operation = False
            while stack and stack[-1] >= item:
                if stack[-1] > item:
                    if not operation:
                        ans += stack[-1] - item
                        operation = True
                stack.pop()
            stack.append(item)
        return ans


target = [1,2,3,2,1]
target = [3,3,1,3,2]
target = [5,5,6,1,2,3,1,3,1,2]
target = [5,5,6,1]
target = [100]
target = [100,23,4,5,6,7,1,12,12,3,3,3,3,6,7,8,9,1,2,3,4,5,1]

solution = Solution()
print(solution.min_number_operation(target))

