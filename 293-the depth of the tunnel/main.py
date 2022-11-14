class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    def find_depth(self, matrix):
        #
        def reach(matrix, row):
            for item in matrix[row]:
                if item == 1:
                    return True
            return False

        left = 0
        right = len(matrix) - 1
        while left + 1 < right:
            middle = (left + right) // 2
            if reach(matrix, middle):
                left = middle
            else:
                right = middle - 1

        if reach(matrix, right):
            return right
        else:
            return left


matrix = [[1,0,0,0,1],[1,1,0,0,1],[0,1,0,1,1],[0,1,1,1,0],[0,0,0,0,0]]
matrix = [[1,0,0,0,0,0,0,1],[1,0,1,1,1,0,0,1],[1,1,1,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

solution = Solution()
print(solution.find_depth(matrix))
