class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def least_interval(self, tasks, n):
        # write your code here
        from collections import defaultdict
        dicts = defaultdict(int)

        for task in tasks:
            dicts[task] += 1

        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)

        for task in dicts:
            heappush(heap, dicts[task] * -1)

        ans = 0
        separators = heappop(heap) * -1
        spares = (separators - 1) * n
        ans += spares + separators
        processed = list()

        while heap and spares > 0:
            availables = heappop(heap) * -1
            fills = min(spares, min(separators - 1, availables))
            if availables > fills:
                processed.append(availables - fills)
            spares -= fills

        for _ in processed:
            heappush(heap, _ * -1)

        ans -= sum(heap)
        return ans

tasks = ['A','A','A','B','B','B']
n = 2

tasks = ['A','A','A','B','B','B']
n = 1

tasks = ['A','A','A','A','B','B','C','D']
n = 2

tasks = ['A','A','A','A','B','B','B','C','C','D','D']
n = 2

solution = Solution()
print(solution.least_interval(tasks, n))
