# @leet start


class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        # tmp = 0
        # i = low
        # jump = 2
        # if low % 2 == 0:
        #     i += 1
        #     # tmp += 1
        #
        # while i <= high:
        #     tmp += 1
        #     # print(i)
        #     i += jump
        #
        # return tmp
        # if high == low and high % 2 == 0:
        #     return 0
        # elif high == low and high % 2 != 0:
        #     return 1

        tmp = high - low

        tmp //= 2
        if low % 2 == 0 and high % 2 == 0:
            tmp -= 1

        # elif low % 2 != 0 and high % 2 == 0:
        #     tmp += 1
        #
        # elif tmp % 2 == 0 and low % 2 != 0 and high % 2 != 0:
        #     tmp += 1

        return int(tmp) + 1


# @leet end
sol = Solution()
low = 100
high = 110

# low = 3
# high = 7

# low = 11
# high = 13
print(sol.countOdds(low, high))
