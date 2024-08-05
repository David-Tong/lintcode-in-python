class Solution:
    """
    @param n: The total number of stones.
    @param m: The total number of stones you can remove.
    @param target: The distance from the end to the starting point.
    @param d: The array that the distance from the i rock to the starting point is d[i].
    @return: Return the maximum value of the shortest jump distance.
    """

    def get_distance(self, n, m, target, d):
        # Write your code here.
        def can_get(search):
            removal = 0
            idx = 0
            while idx < N - 1:
                idx2 = idx + 1
                while idx2 < N and d[idx] + search > d[idx2]:
                    removal += 1
                    idx2 += 1
                idx = idx2
            if removal > m:
                return False
            else:
                return True

        d = [0] + d + [target]
        N = len(d)

        left = 1
        right = 1000000000

        while left + 1 < right:
            middle = (left + right) // 2
            if can_get(middle):
                left = middle
            else:
                right = middle - 1

        if can_get(right):
            return right
        else:
            return left


n = 5
m = 2
target = 25
d = [2,11,14,17,21]

n = 0
m = 0
target = 10
d = []

n = 0
m = 0
target = 65343245
d = []

n = 100
m = 40
target = 53428902
d = [137872,312786,640276,718243,995859,1188568,1229359,1549474,1843642,1931010,2242465,2430010,2549796,2902294,3396266,3521509,3961579,4297275,4613587,4614842,5074008,5094591,5327198,5860009,5945922,6341191,6655012,6816932,7084191,7109821,7640178,7936610,8026301,8054873,8545942,8989726,9224735,9244360,9331817,9406546,9898145,10239978,10764311,10962958,10972250,11128108,11319843,11515655,11818594,12283648,12403800,12631814,12885894,13202229,13229659,13362406,13446983,13639755,13783223,14210368,14292516,14787853,14808906,15269292,15393700,15607344,15858474,16279493,16281697,16551566,16646986,17129598,17270469,17599294,18119162,18371807,18492487,18611563,18843930,18927526,19164215,19465972,19637549,19973483,20262894,20600381,20736572,21174736,21475457,21824861,21986321,22213204,22705607,22708998,23140278,23212977,23378634,23677390,23708887,23728739]

solution = Solution()
print(solution.get_distance(n, m, target, d))
