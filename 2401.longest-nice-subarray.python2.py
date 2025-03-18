# @leet start
class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        usedBits = 0
        maxLength = 0

        for r in range(len(nums)):
            while (usedBits & nums[r]) != 0:
                usedBits ^= nums[l]
                l += 1

            usedBits |= nums[r]
            maxLength = max(maxLength, r - l + 1)

        return maxLength


# @leet end

sol = Solution()
nums = [1, 3, 8, 48, 10]
# nums = [3, 1, 5, 11, 13]
# nums = [
#     744437702,
#     379056602,
#     145555074,
#     392756761,
#     560864007,
#     934981918,
#     113312475,
#     1090,
#     16384,
#     33,
#     217313281,
#     117883195,
#     978927664,
# ]
print(sol.longestNiceSubarray(nums))
