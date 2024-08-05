class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def find_order(self, num_courses, prerequisites):
        # write your code here
        # pre-process
        from collections import defaultdict
        dependents =defaultdict(list)
        ingresses = [0] * num_courses
        for prerequisite in prerequisites:
            ingresses[prerequisite[0]] += 1
            dependents[prerequisite[1]].append(prerequisite[0])

        # bfs
        from collections import deque
        bfs = deque()
        for course in range(num_courses):
            if ingresses[course] == 0:
                bfs.append(course)

        # process
        ans = list()
        while bfs:
            course = bfs.popleft()
            ans.append(course)
            for dependent in dependents[course]:
                ingresses[dependent] -= 1
                if ingresses[dependent] == 0:
                    bfs.append(dependent)

        # check
        for course in range(num_courses):
            if ingresses[course] != 0:
                return list()
        return ans


n = 2
prerequisites = [[1,0]]

n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

solution = Solution()
print(solution.find_order(n, prerequisites))
