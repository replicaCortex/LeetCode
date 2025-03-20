# @leet start
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        for start, end in zip(range(len(nums)), range(3, len(nums) + 1)):
            if nums[start] != 1:
                nums_window = nums[start:end]
                if 0 in nums_window:
                    ans += 1
                    for current_num in range(start, end):
                        if nums[current_num] != 1:
                            nums[current_num] = 1
                        else:
                            nums[current_num] = 0

        return ans if 0 not in nums else -1


# @leet end
sol = Solution()
# nums = [0, 1, 1, 1, 0, 0]

nums = [0, 1, 1, 1]
print(sol.minOperations(nums))
