class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copy_books(self, pages, k):
        # write your code here
        def can_copy_books(pages, k, time):
            copied_pages = 0
            used_people = 1
            for page in pages:
                if page > time:
                    return False
                if copied_pages + page > time:
                    used_people += 1
                    copied_pages = page
                else:
                    copied_pages += page
                if used_people > k:
                    return False
            return True

        L = len(pages)
        if L == 0:
            return 0

        left = 0
        right = sum(pages)

        while left + 1 < right:
            middle = (left + right) // 2
            if can_copy_books(pages, k, middle):
                right = middle
            else:
                left = middle + 1

        if can_copy_books(pages, k, left):
            return left
        elif can_copy_books(pages, k, right):
            return right


pages = [3, 2, 4]
k = 2

"""
pages = [3, 2, 4]
k = 3
"""

solution = Solution()
print(solution.copy_books(pages, k))
