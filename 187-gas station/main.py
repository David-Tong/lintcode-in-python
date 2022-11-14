class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def can_complete_circuit(self, gas, cost):
        # write your code here
        L = len(gas)

        def can_circuit(start):
            steps = 0
            oil = 0
            while steps < L:
                station = (start + steps) % L
                oil += gas[station] - cost[station]
                if oil < 0:
                    return (False, start + steps)
                steps += 1
            return (True, 0)

        start = 0
        while start < L:
            can, station = can_circuit(start)
            if can:
                return start
            else:
                start = station + 1
        return -1


gas = [1,1,3,1]
cost = [2,2,1,1]

gas = [1,1,3,1]
cost = [2,2,10,1]

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas = [2,3,4]
cost = [3,4,3]

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

solution = Solution()
print(solution.can_complete_circuit(gas, cost))
