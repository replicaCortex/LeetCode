# @leet start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        return pow(x, n)


# @leet end


sol = Solution()
x = 2
n = 10
print(sol.myPow(x, n))
