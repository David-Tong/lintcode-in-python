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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root):
        # write your code here
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)
        ans = list()
        while bfs:
            level = list()
            for _ in range(len(bfs)):
                node = bfs.popleft()
                level.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            ans.append(level)

        ans = ans[::-1]
        return ans


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node.left = node2
node.right = node3
"""

node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.level_order_bottom(node))
