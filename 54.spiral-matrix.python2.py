# @leet start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "*"

            if (
                not 0 <= x + dx < cols
                or not 0 <= y + dy < rows
                or matrix[y + dy][x + dx] == "*"
            ):
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res


# @leet end

sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.spiralOrder(matrix))
