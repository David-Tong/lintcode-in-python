class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plus_one(self, head):
        # Write your code here
        digits = list()

        node = head
        while node:
            digits.append(node)
            node = node.next

        L = len(digits)
        carry = 1
        for x in range(L - 1, -1, -1):
            result = digits[x].val + carry
            if result == 10:
                digits[x].val = 0
                carry = 1
            else:
                digits[x].val = result
                carry = 0
                return head

        if carry == 1:
            new = ListNode(1)
            new.next = head

        return new


node = ListNode(9)
node2 = ListNode(9)
node.next = node2

solution = Solution()
node = solution.plus_one(node)

node
