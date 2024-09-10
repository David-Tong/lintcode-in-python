"""
from lintcode import (
    UndirectedGraphNode,
)
"""

# Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node):
        # write your code here
        # short cut
        if not node:
            return

        from collections import deque
        bfs = deque()
        from collections import defaultdict
        visited = defaultdict(bool)

        node_cloned = UndirectedGraphNode(node.label)
        cloneds = defaultdict(UndirectedGraphNode)
        cloneds[node.label] = node_cloned
        bfs.append((node, node_cloned))
        visited[node.label] = True

        # bfs
        while bfs:
            curr, cloned = bfs.popleft()
            for neighbor in curr.neighbors:
                if not visited[neighbor.label]:
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloneds[neighbor.label] = cloned_neighbor
                    bfs.append((neighbor, cloned_neighbor))
                    visited[neighbor.label] = True
                cloned.neighbors.append(cloneds[neighbor.label])

        return node_cloned


node = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(4)

node.neighbors.append(node2)
node.neighbors.append(node3)
node2.neighbors.append(node)
node2.neighbors.append(node3)
node3.neighbors.append(node)
node3.neighbors.append(node2)

solution = Solution()
cloned_node = solution.clone_graph(node)

cloned_node
