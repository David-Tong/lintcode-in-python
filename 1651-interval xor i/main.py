from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param a:
    @param query:
    @return:
    """

    def interval_x_o_r(self, a, query):
        #
        N = len(a)
        prexor = [0] * (N + 1)
        for idx, item in enumerate(a):
            prexor[idx + 1] = prexor[idx] ^ item

        def do_query(qry):
            return prexor[qry.end] ^ prexor[qry.start]

        ans = list()
        for qry in query:
            ans.append(do_query(qry))
        return ans