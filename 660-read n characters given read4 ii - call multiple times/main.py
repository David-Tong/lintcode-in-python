class Reader:
    def reader(self, buf4):
        pass


class Solution:
    def __init__(self):
        self.queue = list()
        self.batch = 4
        self.remain = 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        calls = (n - self.remain + self.batch - 1) // self.batch
        for x in range(calls):
            buf4 = [None] * self.batch
            Reader.read4(buf4)
            for x in range(self.batch):
                if buf4[x]:
                    self.queue.append(buf4[x])

        idx = min(n, len(self.queue))
        buf[0] = "".join(self.queue[:idx])
        self.queue = self.queue[idx:]
        return idx