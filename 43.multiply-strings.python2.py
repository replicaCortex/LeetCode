# @leet start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        return str(int(num2) * int(num1))


# @leet end


sol = Solution()
num1 = "20"
num2 = "3"
print(
    sol.multiply(
        num1,
        num2,
    )
)
