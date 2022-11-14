class Solution:
    """
    @param p1: the first point
    @param p2: the second point
    @param p3: the third point
    @param p4: the fourth point
    @return: whether the four points could construct a square
    """
    def valid_square(self, p1, p2, p3, p4):
        # Write your code here
        def calc_square_distance(p1, p2):
            return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)

        ps = list()
        ps.append(p1)
        ps.append(p2)
        ps.append(p3)
        ps.append(p4)
        L = len(ps)

        from collections import defaultdict
        square_distances = defaultdict(int)
        for x in range(L):
            for y in range(x + 1, L):
                square_distances[calc_square_distance(ps[x], ps[y])] += 1

        if len(square_distances) == 2:
            mini = min(square_distances.keys())
            maxi = max(square_distances.keys())
            if square_distances[mini] == 4 and square_distances[maxi] == 2:
                if maxi == mini * 2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

p1 = [0,0]
p2 = [1,2]
p3 = [1,-1]
p4 = [0,1]

solution = Solution()
print(solution.valid_square(p1, p2, p3, p4))
