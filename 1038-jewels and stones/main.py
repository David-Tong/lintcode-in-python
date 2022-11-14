class Solution:
    """
    @param j: the types of stones that are jewels
    @param s: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def num_jewels_in_stones(self, j, s):
        # Write your code here
        jewels = set()
        for jewel in j:
            jewels.add(jewel)

        ans = 0
        for stone in s:
            if stone in jewels:
                ans += 1

        return ans


j = "aA"
s = "aAAbbbb"

j = "z"
s = "ZZ"

solution = Solution()
print(solution.num_jewels_in_stones(j, s))
