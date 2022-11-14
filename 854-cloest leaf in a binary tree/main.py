class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def find_closest_leaf(self, root, k):
        # Write your code here
        self.parents = list()
        self.target = None

        def find_k(node, parents, k):
            if node.val == k:
                self.target = node
                self.parents = parents
                return
            else:
                if node.left:
                    find_k(node.left, parents + [node], k)
                if node.right:
                    find_k(node.right, parents + [node], k)

        find_k(root, list(), k)

        L = len(self.parents)
        from collections import defaultdict
        paths = defaultdict(TreeNode)

        if L > 0:
            paths[self.target] = self.parents[-1]
            for x in range(len(self.parents) - 1, 0, -1):
                paths[self.parents[x]] = self.parents[x - 1]

        from collections import deque
        bfs = deque()
        bfs.append(self.target)
        vistied = set()
        vistied.add(self.target)

        while bfs:
            L = len(bfs)
            for x in range(L):
                curr = bfs.popleft()
                if curr.left is None and curr.right is None:
                    return curr.val
                else:
                    if curr.left and curr.left not in vistied:
                        bfs.append(curr.left)
                        vistied.add(curr.left)
                    if curr.right and curr.right not in vistied:
                        bfs.append(curr.right)
                        vistied.add(curr.right)
                    if curr in paths and paths[curr] not in vistied:
                        bfs.append(paths[curr])
                        vistied.add(paths[curr])


node = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)

node.left = node2
node.right = node3

k = 1

"""
node = TreeNode(1)
k = 1
"""

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7
node6.left = node8
node7.right = node9
node8.left = node10
node9.right = node11

k = 4
"""

solution = Solution()
print(solution.find_closest_leaf(node, k))



