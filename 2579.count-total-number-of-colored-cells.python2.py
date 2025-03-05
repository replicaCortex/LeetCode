# @leet start
class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 2 * n**2 - 2 * n + 1


# @leet end

sol = Solution()
n = 4
print(sol.coloredCells(n))
