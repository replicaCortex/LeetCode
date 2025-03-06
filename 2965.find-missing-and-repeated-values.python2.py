# @leet start
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        size = n * n
        freq = [0] * (size + 1)
        repeated = -1
        missing = -1

        for row in grid:
            for num in row:
                freq[num] += 1

        for num in range(1, size + 1):
            if freq[num] == 2:
                repeated = num
            if freq[num] == 0:
                missing = num

        return [repeated, missing]


# @leet end

sol = Solution()
grid = [[1, 3], [2, 2]]
grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
# grid = [[2, 2], [3, 4]]
print(sol.findMissingAndRepeatedValues(grid))
