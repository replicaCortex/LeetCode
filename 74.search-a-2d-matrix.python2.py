# @leet start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def _SearchInRow(left=0, right=0, row=[]):
            middle = (left + right) // 2

            if row[middle] == target:
                return True

            elif right < left:
                return False

            elif row[middle] > target:
                return _SearchInRow(right=middle - 1, left=left, row=row)

            elif row[middle] <= target:
                return _SearchInRow(right=right, left=middle + 1, row=row)

        def _SearchInMatrix(left=0, right=0):
            middle = (left + right) // 2

            if matrix[middle][-1] >= target and matrix[middle][0] <= target:
                return _SearchInRow(
                    left=0, right=len(matrix[middle]), row=matrix[middle]
                )

            elif left > right:
                return False

            elif matrix[middle][-1] > target:
                return _SearchInMatrix(right=middle - 1, left=left)

            elif matrix[middle][-1] <= target:
                return _SearchInMatrix(right=right, left=middle + 1)

        return _SearchInMatrix(left=0, right=len(matrix) - 1)


# @leet end
sol = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 23

matrix = [[1, 3, 5]]
target = 1

matrix = [[1]]
target = 0
print(sol.searchMatrix(matrix, target))
