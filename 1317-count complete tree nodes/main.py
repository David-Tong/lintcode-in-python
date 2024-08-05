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
    @param root: root of complete binary tree
    @return: the number of nodes
    """
    def count_nodes(self, root):
        # write your code here
        # bfs
        from collections import deque
        queue = deque()
        if root:
            queue.append(root)

        ans = 0
        while queue:
            curr = queue.popleft()
            ans += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return ans

