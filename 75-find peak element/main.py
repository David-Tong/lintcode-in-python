class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a):
        # write your code here
        def do_find(left, right):
            if left + 1 >= right:
                if 0 < left < N - 1:
                    if a[left - 1] < a[left] > a[left + 1]:
                        return left
                if 0 < right < N - 1:
                    if a[right - 1] < a[right] > a[right + 1]:
                        return right
                return -1

            ans = -1
            middle = (left + right) // 2
            if a[left] >= a[middle]:
                ans = do_find(left, middle)
            elif a[middle] <= a[right]:
                ans = do_find(middle, right)
            else:
                ans = do_find(left, middle)
                if ans != -1:
                    return ans
                ans = do_find(middle, right)
            return ans

        N = len(a)
        return do_find(0, N - 1)


A = [1,2,1,3,4,5,7,6]
#A = [1,2,3,4,1]
#A = [1,2,1]
#A = [1,2,1,2,1]
#A = [1,10,9,8,7,6,5,4]


solution = Solution()
print(solution.find_peak(A))
