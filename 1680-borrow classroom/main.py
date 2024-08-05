class Solution:
    """
    @param r: the number of classrooms available for rent
    @param d: the number of classrooms you need to borrow
    @param s: the start day you borrow the classroom
    @param t: the end day you borrow the classroom
    @return: which applicant to modify the order
    """
    def get_applicant(self, r, d, s, t):
        # Write your code here.
        R = len(r)
        D = len(d)

        # difference array
        da = [0] * R
        for x in range(R):
            if x == 0:
                da[x] = r[x]
            else:
                da[x] = r[x] - r[x - 1]

        def can_borrow(target):
            from copy import deepcopy
            temp_da = deepcopy(da)
            for idx in range(target):
                temp_da[s[idx] - 1] -= d[idx]
                if t[idx] < D:
                    temp_da[t[idx]] += d[idx]

            # re-construct
            classroom = 0
            for item in temp_da:
                classroom += item
                if classroom < 0:
                    return False
            return True

        left = 1
        right = D

        while left + 1 < right:
            middle = (left + right) // 2
            if can_borrow(middle):
                left = middle
            else:
                right = middle - 1

        ans = -1
        if can_borrow(right):
            ans = right
        elif can_borrow(left):
            ans = left

        return 0 if ans == D else ans


r = [2, 5, 4, 3]
d = [2, 3, 4]
s = [1, 2, 2]
t = [3, 4, 4]

r = [2, 2]
d = [2]
s = [1]
t = [2]

r = [42323424,633675939,990396626,965164370,965164370,965164370,972489810,619351082,619351082,0]
d = [586780256,316471206,42323424,8081621,36667522,110729,4572259,7436169,3834281,8646496]
s = [2,3,1,3,3,3,2,7,3,4]
t = [9,7,3,9,7,6,9,9,9,9]

solution = Solution()
print(solution.get_applicant(r, d, s, t))
