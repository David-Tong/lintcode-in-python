class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param k: the given K
    @return: All Nodes Distance K in Binary Tree
             we will sort your return value in output
    """
    def __init__(self):
        self.parents = list()
        self.anses = list()

    def __find_target(self, node, target, parents):
        if node.val == target.val:
            self.parents = parents + [node]
        else:
            if node.left:
                self.__find_target(node.left, target, parents + [node])
            if node.right:
                self.__find_target(node.right, target, parents + [node])

    def __search_answers(self, node, k):
        if k == 0:
            self.anses.append(node.val)
            return

        from collections import deque
        bfs = deque()
        bfs.append((node, 0))
        while bfs:
            curr, dist = bfs.popleft()
            if curr.left:
                if curr.left not in self.parents:
                    if dist + 1 == k:
                        self.anses.append(curr.left.val)
                    bfs.append((curr.left, dist + 1))
            if curr.right:
                if curr.right not in self.parents:
                    if dist + 1 == k:
                        self.anses.append(curr.right.val)
                    bfs.append((curr.right, dist + 1))

    def distance_k(self, root, target, k):
        self.__find_target(root, target, [])
        N = len(self.parents)

        for idx, parent in enumerate(self.parents):
            self.__search_answers(parent, k - (N - idx - 1))

        return self.anses


node = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9

target = node2
k = 2

"""
node = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node.left = node2
node.right = node3
node2.left = node4

target = node2
k = 1
"""
"""
node = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(1)
node4 = TreeNode(3)

node.left = node2
node.right = node3
node3.left = node4

target = node4
k = 3
"""

solution = Solution()
print(solution.distance_k(node, target, k))
