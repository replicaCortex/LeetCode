# @leet start
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums, reverse=False)

        perimeter = [0]
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                perimeter.append(nums[i] + nums[i + 1] + nums[i + 2])

        return max(perimeter)


# @leet end


sol = Solution()
# nums = [2, 1, 2]
nums = [3, 2, 3, 4]
# nums = [1, 2, 1, 10]
print(sol.largestPerimeter(nums))
