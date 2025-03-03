# @leet start
class Solution:
    def pivotArray(self, nums, pivot):
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1

            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1

        while left <= right:
            result[left] = pivot
            left += 1

        return result

        # tmp = [pivot]
        # pivot_index = 0
        #
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         tmp.insert(pivot_index, nums[i])
        #         pivot_index += 1
        #     elif nums[i] == pivot:
        #         tmp.insert(pivot_index, nums[i])
        #     else:
        #         tmp.append(nums[i])
        #
        # del tmp[pivot_index]
        # return tmp

        # small, middle, large = [], [], []
        # for i in range(len(nums)):
        #     if nums[i] < pivot:
        #         small.append(nums[i])
        #     elif nums[i] > pivot:
        #         large.append(nums[i])
        #     else:
        #         middle.append(nums[i])
        #
        # return small + middle + large


# @leet end


sol = Solution()
# nums = [9, 12, 5, 10, 14, 3, 10]
# pivot = 10

nums = [-3, 4, 3, 2]
pivot = 2
print(sol.pivotArray(nums, pivot))
