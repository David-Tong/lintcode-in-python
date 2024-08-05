# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        self.ans = None
        def lca(node, A , B):
            if not node:
                return False

            lca_left = lca(node.left, A, B)
            lca_right = lca(node.right, A, B)

            if node == A or node == B:
                if lca_left or lca_right:
                    self.ans = node
                return True
            else:
                if lca_left and lca_right:
                    self.ans = node
                return lca_left or lca_right

        # shortcut
        if A == B:
            return A

        lca(root, A, B)
        return self.ans


"""
node = TreeNode(1)
"""

node = TreeNode(4)
node2 = TreeNode(3)
node3 = TreeNode(7)
node4 = TreeNode(5)
node5 = TreeNode(6)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
ans = solution.lowestCommonAncestor(node, node4, node5)

ans
