# @leet start
class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        non_zero_idx = 0

        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1

        for i in range(non_zero_idx, n):
            nums[i] = 0

        return nums


# @leet end

sol = Solution()
nums = [1, 2, 2, 1, 1, 0]
# nums = [0, 2, 2, 1, 1, 0]
# nums = [0, 0, 2, 1, 1, 0]
print(sol.applyOperations(nums))
