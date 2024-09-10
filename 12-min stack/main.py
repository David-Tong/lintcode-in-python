class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = list()
        self.monotonic = list()

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.monotonic or self.monotonic[-1] >= number:
            self.monotonic.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.stack:
            number = self.stack.pop()
            if self.monotonic and self.monotonic[-1] == number:
                self.monotonic.pop()
            return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if self.monotonic:
            return self.monotonic[-1]


"""
min_stack = MinStack()
min_stack.push(3)
print(min_stack.min())
min_stack.push(2)
print(min_stack.min())
min_stack.push(1)
print(min_stack.min())
print(min_stack.pop())
print(min_stack.min())
print(min_stack.pop())
print(min_stack.min())
"""

min_stack = MinStack()
min_stack.push(1)
print(min_stack.pop())
min_stack.push(2)
min_stack.push(3)
print(min_stack.min())
min_stack.push(1)
print(min_stack.min())



