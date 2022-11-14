class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """
    def find_bottom_left_value(self, root):
        # write your code here
        from collections import deque
        bfs = deque()
        bfs.append(root)

        ans = None
        while bfs:
            for x in range(len(bfs)):
                curr = bfs.popleft()
                if x == 0:
                    ans = curr
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
        return ans.val

"""
node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node.left = node2
node.right = node3
"""

node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.right = node7

solution = Solution()
print(solution.find_bottom_left_value(node))
