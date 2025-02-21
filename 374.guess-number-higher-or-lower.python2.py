# @leet start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num, pick):
#     if num > pick:
#         return -1
#     elif num < pick:
#         return 1
#     else:
#         return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        def Search(right=n, left=0):
            middle = (right + left) // 2
            guess_output = guess(middle)

            if guess_output == -1:
                return Search(right=middle - 1, left=left)
            elif guess_output == 1:
                return Search(right=right, left=middle + 1)
            else:
                return middle

        return Search()


# @leet end

sol = Solution()
n = 10
pick = 0
print(sol.guessNumber(n))
