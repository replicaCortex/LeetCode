# @leet start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def Search(right=x, left=0):
            middle = (right + left) // 2
            if middle * middle == x:
                return middle

            elif middle * middle >= x and (middle - 1) * (middle - 1) <= x:
                return middle - 1

            # elif middle * middle == x - 1:
            #     return middle - 1

            elif middle * middle > x:
                return Search(right=middle - 1, left=left)

            elif middle * middle <= x:
                return Search(right=right, left=middle + 1)

        return Search()


# @leet end

sol = Solution()
x = 4
# x = 8
# x = 9
# x = 10
# x = 11
# x = 15
# x = 18
# x = 101
# x = 16
print(sol.mySqrt(x))
