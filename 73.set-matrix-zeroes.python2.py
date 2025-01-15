# @leet start


class Solution:
    def setZeroes(self, matrix):
        """
        Модифицирует матрицу таким образом, что если элемент равен 0,
        то весь соответствующий столбец и строка становятся 0.
        """
        n = len(matrix)  # Количество строк
        m = len(matrix[0])  # Количество столбцов

        # Множества для хранения строк и столбцов, содержащих 0
        set_rows = set()
        set_columns = set()

        # Первый проход: находим строки и столбцы, где есть 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    set_rows.add(i)  # Добавляем индекс строки
                    set_columns.add(j)  # Добавляем индекс столбца

        # Второй проход: обновляем матрицу
        for i in range(n):
            for j in range(m):
                if i in set_rows or j in set_columns:
                    matrix[i][j] = 0


# @leet end


sol = Solution()
# matrix = [[1, 1, 0], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(sol.setZeroes(matrix))
