class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        from collections import defaultdict
        self.parents = defaultdict(TreeNode)
        self.children = defaultdict(int)
        from collections import deque
        self.leaves = deque()

        def findParents(node, parent):
            if parent:
                self.parents[node] = parent

            if node.left is None and node.right is None:
                self.leaves.append(node)
            else:
                if node.left:
                    self.children[node] += 1
                    findParents(node.left, node)

                if node.right:
                    self.children[node] += 1
                    findParents(node.right, node)

        if root is None:
            return list()

        findParents(root, None)

        anses = list()
        while self.leaves:
            L = len(self.leaves)
            ans = list()
            for x in range(L):
                curr = self.leaves.popleft()
                ans.append(curr.val)
                if curr in self.parents and self.parents[curr] in self.children:
                    self.children[self.parents[curr]] -= 1
                    if self.children[self.parents[curr]] == 0:
                        self.leaves.append(self.parents[curr])
            anses.append(ans)
        return anses


"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
"""

node = TreeNode(1)

solution = Solution()
print(solution.findLeaves(node))
