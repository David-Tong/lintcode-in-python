class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root):
        # write your code here
        self.anses = list()

        def do_paths(node, path):
            if not node.left and not node.right:
                self.anses.append(path + str(node.val))
            else:
                if node.left:
                    do_paths(node.left, path + str(node.val) + "->")
                if node.right:
                    do_paths(node.right, path + str(node.val) + "->")

        if root:
            do_paths(root, "")
            return self.anses
        else:
            return list()


node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(5)

node.left = node2
node.right = node3
node2.right = node4

solution = Solution()
print(solution.binary_tree_paths(node))