# @leet start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        if moves.count("R") == moves.count("L") and moves.count(
            "U"
        ) == moves.count("D"):
            return True

        return False


# @leet end


sol = Solution()
moves = "UD"

# moves = "RRDD"
# moves = "ULRDULDR"
print(sol.judgeCircle(moves))
