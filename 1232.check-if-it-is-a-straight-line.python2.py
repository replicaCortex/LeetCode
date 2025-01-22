# @leet start
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if (y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1):
                return False
        return True


# @leet end

sol = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# coordinates = [[0, 0], [0, 1], [0, -1]]

print(sol.checkStraightLine(coordinates))
