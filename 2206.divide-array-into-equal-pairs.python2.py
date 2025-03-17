# @leet start
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)

        for num in nums_set:
            if nums.count(num) % 2 != 0:
                return False

        return True


# @leet end
sol = Solution()
nums = [3, 2, 3, 2, 2, 2]
print(sol.divideArray(nums))
