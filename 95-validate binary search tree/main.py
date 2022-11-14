class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root):
        # write your code here
        def do_validate(node):
            MIN = node.val
            MAX = node.val

            if node.left:
                valid, LMIN, LMAX = do_validate(node.left)
                if not valid or LMAX >= node.val:
                    return False, None, None
                MIN = min(LMIN, node.val)

            if node.right:
                valid, RMIN, RMAX = do_validate(node.right)
                if not valid or RMIN <= node.val:
                    return False, None, None
                MAX = max(RMAX, node.val)

            return True, MIN, MAX

        if root:
            valid, _, _ = do_validate(root)
            return valid
        else:
            return True


"""
node = TreeNode(-1)

node = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(3)
node5 = TreeNode(5)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

node = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(6)
node5 = TreeNode(6)
node6 = TreeNode(9)

node.left = node2
node.right = node3
node2.right = node4
node3.left = node5
node3.right = node6
"""

node = TreeNode(1)
node2 = TreeNode(1)

node.left = node2


solution = Solution()
print(solution.is_valid_b_s_t(node))
