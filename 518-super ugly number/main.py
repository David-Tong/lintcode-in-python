class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nth_super_ugly_number(self, n, primes):
        # write your code here
        # pre-process
        uglies = list()
        ugly = 1
        uglies.append(ugly)
        L = len(primes)
        idxes = [0] * L

        # process
        while len(uglies) < n:
            ugly = float("inf")
            for x in range(L):
                nugly = primes[x] * uglies[idxes[x]]
                if ugly > nugly:
                    ugly = nugly
                    idx = x

            if ugly not in uglies:
                uglies.append(ugly)
            idxes[idx] += 1

        return ugly


n = 6
primes = [2,7,13,19]

n = 11
primes = [2,3,5]

n = 100
primes = [2,7,13,19]

solution = Solution()
print(solution.nth_super_ugly_number(n, primes))
