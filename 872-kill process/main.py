class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
             we will sort your return value in output
    """
    def kill_process(self, pid, ppid, kill):
        # Write your code here
        from collections import defaultdict
        ptree = defaultdict(list)

        for idx in range(len(pid)):
            ptree[ppid[idx]].append(pid[idx])

        from collections import deque
        bfs = deque()
        ans = list()
        bfs.append(kill)

        while bfs:
            curr = bfs.popleft()
            ans.append(curr)
            for child in ptree[curr]:
                bfs.append(child)

        return ans


PID = [1, 3, 10, 5]
PPID = [3, 0, 5, 3]
killID = 5

PID = [1, 2, 3]
PPID = [0, 1, 1]
killID = 2

solution = Solution()
print(solution.kill_process(PID, PPID, killID))
