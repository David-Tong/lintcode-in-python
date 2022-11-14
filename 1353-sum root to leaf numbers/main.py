class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sum_numbers(self, root):
        # write your code here
        self.totals = list()
        def do_sum(node, paths):
            if not node.left and not node.right:
                paths += str(node.val)
                self.totals.append(paths)
            else:
                if node.left:
                    do_sum(node.left, paths + str(node.val))
                if node.right:
                    do_sum(node.right, paths + str(node.val))

        if root:
            do_sum(root, "")
            print(self.totals)

            ans = 0
            for total in self.totals:
                ans += int(total)
            return ans
        else:
            return 0


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node.left = node2
node.right = node3
"""

"""
node = TreeNode(4)
node2 = TreeNode(9)
node3 = TreeNode(0)
node4 = TreeNode(5)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
"""

node = TreeNode(0)
node2 = TreeNode(9)
node3 = TreeNode(0)
node4 = TreeNode(5)
node5 = TreeNode(1)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5

solution = Solution()
print(solution.sum_numbers(None))
