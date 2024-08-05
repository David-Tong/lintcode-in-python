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
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def right_side_view(self, root):
        # write your code here
        if not root:
            return list()

        from collections import deque
        bfs = deque()
        bfs.append(root)

        ans = list()
        while bfs:
            right = None
            for _ in range(len(bfs)):
                curr = bfs.popleft()
                right = curr.val
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
            ans.append(right)
        return ans


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)
node5 = TreeNode(4)

node.left = node2
node.right = node3
node2.right = node4
node3.right = node5

solution = Solution()
print(solution.right_side_view(None))
