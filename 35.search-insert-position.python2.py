# @leet start


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def Search(nums, target, right=len(nums) - 1, left=0):
            middle = (right + left) // 2

            if right < left:
                return middle + 1

            elif nums[middle] == target:
                return middle

            elif nums[middle] > target:
                return Search(nums, target, right=middle - 1, left=left)

            elif nums[middle] <= target:
                return Search(nums, target, right=right, left=middle + 1)

            return middle

        return Search(nums, target)


# @leet end

sol = Solution()
nums = [1, 3, 5, 6]
target = 20
print(sol.searchInsert(nums, target))
