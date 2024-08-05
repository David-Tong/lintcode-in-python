# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)
        tree = list()

        while bfs:
            curr = bfs.popleft()
            if curr:
                tree.append(curr.val)
                if curr.left:
                    bfs.append(curr.left)
                else:
                    bfs.append(None)
                if curr.right:
                    bfs.append(curr.right)
                else:
                    bfs.append(None)
            else:
                tree.append("#")

        while tree and tree[-1] == "#":
            tree.pop()

        return tree

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data:
            root = TreeNode(data[0])
        else:
            root = None

        from collections import deque
        bfs = deque()
        bfs.append(root)

        idx = 1
        while bfs:
            curr = bfs.popleft()
            if idx < len(data):
                if data[idx] != "#":
                    curr.left = TreeNode(data[idx])
                    bfs.append(curr.left)
                idx += 1
            else:
                break
            if idx < len(data):
                if data[idx] != "#":
                    curr.right = TreeNode(data[idx])
                    bfs.append(curr.right)
                idx += 1
            else:
                break

        return root


node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.left = node2
node.right = node3
node3.left = node4
node3.right = node5

node = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node.right = node2
node2.right = node3
node3.right = node4
node4.right = node5

#node = None

solution = Solution()
tree = solution.serialize(node)
print(tree)
root = solution.deserialize(tree)

root
