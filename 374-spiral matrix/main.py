class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiral_order(self, matrix):
        # write your code here
        if type(matrix) != list:
            return 0
        M = len(matrix)

        if M > 0:
            if type(matrix[0]) != list:
                return []
        else:
            return []
        N = len(matrix[0])

        self.ans = list()

        def do_spiral(matrix, top, left, bottom, right):
            if top < bottom and left < right:
                # from left to right
                for x in range(left, right + 1):
                    self.ans.append(matrix[top][x])
                # from top to bottom
                for x in range(top + 1, bottom):
                    self.ans.append(matrix[x][right])
                # from right to left
                for x in range(right, left - 1, -1):
                    self.ans.append(matrix[bottom][x])
                # from bottom to top
                for x in range(bottom - 1 , top, -1):
                    self.ans.append(matrix[x][left])
                do_spiral(matrix, top + 1, left + 1, bottom - 1, right - 1)
            elif top == bottom and left == right:
                self.ans.append(matrix[top][left])
            elif top == bottom:
                for x in range(left, right + 1):
                    self.ans.append(matrix[top][x])
            elif left == right:
                for x in range(top, bottom + 1):
                    self.ans.append(matrix[x][left])
            else:
                return

        if M == 0 or N == 0:
            pass
        else:
            do_spiral(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        return self.ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[6,4,1],[7,8,9]]
matrix = [[1,2,3]]
matrix = [[1],[2],[3]]
matrix = [[1]]
matrix = [[]]
matrix = []

solution = Solution()
print(solution.spiral_order(matrix))
