# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # step 1
        # create a list with copy nodes
        #   1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        curr = head
        while curr:
            nxt = curr.next
            copy = RandomListNode(curr.label)
            curr.next = copy
            copy.next = nxt
            curr = nxt

        # step 2
        # copy random pointers
        curr = head
        while curr:
            if curr.random:
                random = curr.random.next
            else:
                random = None
            copy = curr.next
            copy.random = random
            curr = curr.next.next

        # step 3
        # split the list to
        #   1 -> 2 -> 3 -> 4, 1'-> 2'-> 3'-> 4'
        dummy = RandomListNode(0)
        copy = dummy
        curr = head
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            copy = copy.next
        return dummy.next


"""
node = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node4 = RandomListNode(4)

node.next = node2
node.random = node3
node2.next = node3
node2.random = node
node3.next = node4
node3.random = node2
node4.random = node3
"""

node = RandomListNode(-1)
node.random = None

solution = Solution()
ans = solution.copyRandomList(node)

ans
