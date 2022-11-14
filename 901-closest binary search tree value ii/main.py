class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
             we will sort your return value in output
    """
    def closest_k_values(self, root, target, k):
        # write your code here
        # get sorted array
        nums = list()

        def leftMost(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = list()
        leftMost(root, stack)
        while stack:
            node = stack.pop()
            nums.append(node.val)
            leftMost(node.right, stack)

        # do binary search
        L = len(nums)

        from bisect import bisect_left
        idx = bisect_left(nums, target)
        if idx == L:
            left = idx - 1
            right = idx
        elif idx == 0:
            left = idx
            right = idx + 1
        else:
            left = idx
            right = idx + 1

        ans = list()
        for x in range(k):
            if left >= 0:
                delta_left = abs(target - nums[left])
            else:
                delta_left = float("inf")

            if right < len(nums):
                delta_right = abs(target - nums[right])
            else:
                delta_right = float("inf")

            if delta_left <= delta_right:
                ans.append(nums[left])
                left -= 1
            else:
                ans.append(nums[right])
                right += 1
        return ans


solution = Solution()

"""
node = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(2)

node.left = node2
node.right = node3
node2.right= node4

target = 0.275000
k = 2
"""

node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node.left = node2
node.right = node3

target = 5.571429
k = 2

print(solution.closest_k_values(node, target, k))
