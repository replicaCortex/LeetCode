# @leet start
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            result = len(nums)

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    result = mid
                    right = mid - 1

            return result

        neg_count = binary_search(nums, 0)
        pos_count = len(nums) - binary_search(nums, 1)
        return max(neg_count, pos_count)


# @leet end

sol = Solution()
nums = [-2, -1, -1, 1, 2, 3]
print(sol.maximumCount(nums))
