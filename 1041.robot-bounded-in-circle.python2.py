# @leet start


class Solution(object):
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "R":
                dx, dy = dy, -dx
            if i == "L":
                dx, dy = -dy, dx
            if i == "G":
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


# @leet end

sol = Solution()
instructions = "GGLLGG"
instructions = "GLRLLGLL"
print(sol.isRobotBounded(instructions))
