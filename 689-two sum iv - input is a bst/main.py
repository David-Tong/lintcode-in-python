# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        def leftMost(node):
            while node:
                stack.append(node)
                node = node.left

        def searchTarget(node, target):
            if node and node != target:
                if node.val == n - target.val:
                    return True
                elif node.val < n - target.val:
                    return searchTarget(node.right, target)
                else:
                    return searchTarget(node.left, target)
            else:
                return False


        stack = list()
        leftMost(root)

        while stack:
            node = stack.pop()
            if searchTarget(root, node):
                return node.val, n - node.val
            leftMost(node.right)

        return None


"""
node = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(3)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

n = 3
n = 5
n = 10
"""

node = TreeNode(100)
node2 = TreeNode(10)
node3 = TreeNode(101)
node4 = TreeNode(2)
node5 = TreeNode(11)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

n = 13

solution = Solution()
print(solution.twoSum(node, n))

