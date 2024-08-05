# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        # Write your code here.
        from collections import deque
        bfs = deque()
        bfs.append((root, root.val, [root.val]))

        ans = list()
        while bfs:
            curr, val, path = bfs.popleft()
            if curr.left:
                bfs.append((curr.left, val + curr.left.val, path + [curr.left.val]))
                if val + curr.left.val == sum:
                    if not curr.left.left and not curr.left.right:
                        ans.append(path + [curr.left.val])
            if curr.right:
                bfs.append((curr.right, val + curr.right.val, path + [curr.right.val]))
                if val + curr.right.val == sum:
                    if not curr.right.left and not curr.right.right:
                        ans.append(path + [curr.right.val])
        return ans


node = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(9)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10

sum = 22

solution = Solution()
print(solution.pathSum(node, sum))
