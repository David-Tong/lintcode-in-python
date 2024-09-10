"""
from lintcode import (
    TreeNode,
)
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root, k1, k2):
        # write your code here
        # in-order traverse
        stack = list()
        def left_most(node):
            while node:
                stack.append(node)
                node = node.left
        left_most(root)
        ans = list()
        while stack:
            node = stack.pop()
            # check if in range[k1, k2]
            if node.val > k2:
                break
            elif node.val >= k1:
                ans.append(node.val)
            left_most(node.right)
        return ans


"""
node = TreeNode(5)
k1 = 6
k2 = 10
"""

"""
node = TreeNode(20)
node2 = TreeNode(8)
node3 = TreeNode(22)
node4 = TreeNode(4)
node5 = TreeNode(12)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

k1 = 10
k2 = 22
"""

node = TreeNode(20)
node2 = TreeNode(2)
node3 = TreeNode(40)
node4 = TreeNode(35)

node.left = node2
node.right = node3
node3.left = node4

k1 = 17
k2 = 37

solution = Solution()
print(solution.search_range(node, k1 , k2))



