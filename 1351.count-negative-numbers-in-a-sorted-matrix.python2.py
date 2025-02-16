# @leet start
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        i = len(grid) - 1
        j = 0
        count = 0
        while i >= 0 and j < len(grid[0]):
            print(i, j)
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return count


# @leet end

sol = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(sol.countNegatives(grid))
