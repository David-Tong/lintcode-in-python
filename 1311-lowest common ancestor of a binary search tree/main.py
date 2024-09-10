# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        # pre-process
        self.ans = None

        def lca(node):
            curr, left, right = False, False, False

            if node.left:
                left = lca(node.left)
            if node.right:
                right = lca(node.right)
            if node.val == p.val or node.val == q.val:
                curr = True
            if curr:
                if left or right:
                    self.ans = node
            else:
                if left and right:
                    self.ans = node

            return left | right | curr

        # shortcut
        if p == q:
            return p

        # process
        lca(root)
        return self.ans


node = TreeNode(6)
node2 = TreeNode(5)
node3 = TreeNode(8)
node4 = TreeNode(0)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(9)
node8 = TreeNode(3)
node9 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

p = node2
q = node3

p = node2
q = node5

p = node4
q = node7

p = node9
q = node9

p = node2
q = node9

solution = Solution()
node = solution.lowestCommonAncestor(node, p, q)

print(node.val)
