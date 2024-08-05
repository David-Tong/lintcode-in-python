class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param k: a integer
    @return: return a integer
    """
    def find_cheapest_price(self, n, flights, src, dst, k):
        # write your code here
        # pre-process
        from collections import defaultdict
        edges = list()
        for _ in range(n):
            edges.append(defaultdict(int))
        for flight in flights:
            edges[flight[0]][flight[1]] = flight[2]
        visited = [float("inf")] * n

        from collections import deque
        bfs = deque()
        bfs.append((src, 0))
        visited[src] = 0

        stops = 0
        while bfs:
            size = len(bfs)
            for x in range(size):
                curr, cost = bfs.popleft()
                for vertex in edges[curr]:
                    new_cost = cost + edges[curr][vertex]
                    if new_cost < visited[vertex]:
                        visited[vertex] = new_cost
                        bfs.append((vertex, new_cost))
            stops += 1
            if stops > k:
                break

        if visited[dst] == float("inf"):
            return -1
        else:
            return visited[dst]


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 0

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1

solution = Solution()
print(solution.find_cheapest_price(n, flights, src, dst, K))
