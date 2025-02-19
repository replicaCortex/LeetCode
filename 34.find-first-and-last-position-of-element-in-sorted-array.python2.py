# @leet start
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         def Search(right=len(nums), left=0, target=0):
#
#             if not nums:
#                 return [-1, -1]
#
#             middle = (right + left) // 2
#
#             if right < left or middle > len(nums) - 1:
#                 return [-1, -1]
#
#             elif nums[middle] == target:
#                 while middle > 0 and nums[middle - 1] == target:
#                     middle -= 1
#
#                 y = x = middle
#                 while middle + 1 < len(nums) and nums[middle + 1] == target:
#                     y += 1
#                     middle += 1
#
#                 return [x, y]
#
#             elif nums[middle] > target:
#                 return Search(right=middle - 1, left=left, target=target)
#
#             elif nums[middle] < target:
#                 return Search(right=right, left=middle + 1, target=target)
#
#         return Search(target=target)


class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = binarySearchLeft(nums, target)
        right_index = binarySearchRight(nums, target)

        # Проверка на наличие target в массиве
        if (
            left_index <= right_index
            and 0 <= left_index < len(nums)
            and nums[left_index] == target
        ):
            return [left_index, right_index]
        else:
            return [-1, -1]


# @leet end

sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
#
# nums = [2, 2]
# target = 3

# nums = [5, 7, 7, 8, 8, 10]
# target = 6

# nums = []
# target = 0

# nums = [1]
# target = 1
print(sol.searchRange(nums, target))
