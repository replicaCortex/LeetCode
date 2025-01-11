# @leet start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        if len(moves) == 1:
            return False

        start = [0, 0]
        for i in range(len(moves)):
            # move Ox

            if moves[i] == "U":
                start[0] = start[0] + 1

            elif moves[i] == "D":
                start[0] = start[0] - 1
            # move Oy

            elif moves[i] == "R":
                start[1] = start[1] + 1

            else:
                start[1] = start[1] - 1

        if start == [0, 0]:
            return True

        return False


# @leet end


sol = Solution()
moves = "UD"

moves = "RRDD"
# moves = "ULRDULDR"
print(sol.judgeCircle(moves))
