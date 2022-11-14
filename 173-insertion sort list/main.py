class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertion_sort_list(self, head):
        # write your code here
        def do_sort(head, insert, index):
            dummy = ListNode("N/A")
            dummy.next = head
            prev = dummy
            curr = dummy.next
            while curr and curr.val < insert.val and curr != insert:
                prev = curr
                curr = curr.next

            prev.next = insert
            if curr != insert:
                insert.next = curr

            steps = 0
            curr = dummy
            while steps < index:
                curr = curr.next
                steps += 1
            curr.next = None

            return dummy.next

        curr = head
        successor = head.next
        index = 1
        while successor:
            tmp = successor.next
            successor.next = None
            index += 1
            head = do_sort(head, successor, index)
            successor = tmp

        return head


"""
node = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(0)

node.next = node2
node2.next = node3
node3.next = node4
"""

"""
node = ListNode(1)
node2 = ListNode(1)

node.next = node2
"""

node = ListNode(2)
node2 = ListNode(1)

node.next = node2

"""
node = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(4)

node.next = node2
node2.next = node3
"""

"""
node = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(1)

node.next = node2
node2.next = node3
"""

solution = Solution()
head = solution.insertion_sort_list(node)

head
