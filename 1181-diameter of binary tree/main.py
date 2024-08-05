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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameter_of_binary_tree(self, root):
        # write your code here
        # return
        #   1. diameter in the subtree
        #   2. diameter out of the subtree
        def do_diameter(node):
            if node:
                left_in_diameter, left_out_of_diameter = do_diameter(node.left)
                right_in_diameter, right_out_of_diameter = do_diameter(node.right)

                in_diameter = max(max(left_in_diameter, right_in_diameter), left_out_of_diameter + right_out_of_diameter + 1)
                out_of_diameter = max(left_out_of_diameter, right_out_of_diameter) + 1

                # print(node.val, in_diameter, out_of_diameter)
                return in_diameter, out_of_diameter
            else:
                return 0, 0

        in_diameter, out_of_diameter = do_diameter(root)
        # print(in_diameter, out_of_diameter)
        ans = max(in_diameter, out_of_diameter) - 1
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
"""

"""
node = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(1)

node.left = node2
node2.left = node3
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node6.right = node7
node5.right = node8
node8.left = node9

solution = Solution()
print(solution.diameter_of_binary_tree(node))
