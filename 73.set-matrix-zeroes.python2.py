# @leet start


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row, cols = len(matrix), len(matrix[0])

        tmp = []
        # for i in range(rows * cols):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    tmp.append([i, j])

        dx, dy = 1, 0
        for i in range(len(tmp)):
            x, y = tmp[i]
            count = 0

            while True:

                if x != row and y != cols:
                    matrix[x][y] = 0

                if abs(x + dx) >= row or abs(y + dy) >= cols:
                    count += 1
                    if count == 4:
                        break

                    x, y = tmp[i]
                    dx, dy = -dy, dx

                # if abs(x + dx) == cols or abs(y + dy) == row:
                #     dx, dy = -dy, dx

                x += dx
                y += dy

        # return matrix


# @leet end


sol = Solution()
# matrix = [[1, 1, 0], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(sol.setZeroes(matrix))
