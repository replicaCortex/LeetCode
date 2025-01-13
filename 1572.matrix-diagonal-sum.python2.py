# @leet start
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat) - 1 - i]

        if len(mat) % 2 != 0:
            sum -= mat[len(mat) // 2][len(mat) // 2]

        return sum


# @leet end

sol = Solution()
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [
    [7, 9, 8, 6, 3],
    [3, 9, 4, 5, 2],
    [8, 1, 10, 4, 10],
    [9, 5, 10, 9, 6],
    [7, 2, 4, 10, 8],
]
print(sol.diagonalSum(mat))
