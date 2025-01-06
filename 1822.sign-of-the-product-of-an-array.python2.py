# @leet start
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if 0 in nums:
            return 0

        tmp = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                tmp += 1

        if tmp % 2 == 0:
            return 1
        else:
            return -1


# sol = Solution()
# nums = [-1, -2, -3, -4, 3, 2, 1]
# nums = [0, -1, -2, -3, -4, 3, 2, 1]
# print(sol.arraySign(nums))
# @leet end
