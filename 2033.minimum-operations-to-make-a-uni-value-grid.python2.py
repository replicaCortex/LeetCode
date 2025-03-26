# @leet start
class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """

        a = [cell for row in grid for cell in row]
        a.sort()
        mid = len(a) // 2
        median = a[mid]
        tc = 0
        for value in a:
            if abs(value - median) % x != 0:
                return -1
            tc += abs(value - median) // x
        return tc


# @leet end

sol = Solution()
grid = [[2, 4], [6, 8]]
x = 2
print(sol.minOperations(grid, x))
