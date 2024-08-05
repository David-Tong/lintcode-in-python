class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def house_robber3(self, root):
        # write your code here
        # stolen - if stolen in parent
        def robber(node, stolen):
            key = str(node) + "-" + str(stolen)
            if key in self.cache:
                return self.cache[key]
            if node is None:
                return 0

            # stolen parent node
            if stolen:
                val = max(robber(node.left, True), robber(node.left, False)) \
                    + max(robber(node.right, True), robber(node.right, False))
            else:
                val = max(node.val + robber(node.left, True) + robber(node.right, True),
                           max(robber(node.left, True), robber(node.left, False))
                           + max(robber(node.right, True), robber(node.right, False)))
            self.cache[key] = val
            return val

        from collections import defaultdict
        self.cache = defaultdict(int)
        return robber(root, False)


"""
node = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(3)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.right = node4
node3.right = node5
"""

node = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

solution = Solution()
print(solution.house_robber3(node))
