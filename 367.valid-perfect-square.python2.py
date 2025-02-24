# @leet start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if int(num**0.5) * int(num**0.5) == num:
            return True
        else:
            return False


# @leet end
sol = Solution()
num = 16
# num = 14
# num = 76
print(sol.isPerfectSquare(num))
