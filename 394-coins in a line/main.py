class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def first_will_win(self, n):
        # write your code here
        return n % 3 != 0