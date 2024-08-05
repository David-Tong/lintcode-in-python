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
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def count_unival_subtrees(self, root):
        # write your code here
        self.ans = 0
        def do_count(node):
            if not node:
                return None

            values = set()
            values.add(node.val)
            if node.left:
                values = values.union(do_count(node.left))
            if node.right:
                values = values.union(do_count(node.right))

            if len(values) == 1:
                self.ans += 1
            return values

        do_count(root)
        return self.ans


node = TreeNode(5)
node2 = TreeNode(1)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(5)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

"""
node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

"""
node = TreeNode(5)
node2 = TreeNode(5)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(5)
node6 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
"""

solution = Solution()
print(solution.count_unival_subtrees(node))
