# @leet start
class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 1
        r = 10**9

        while l < r:
            m, t, i = (l + r) // 2, 0, 0
            while i < len(nums) and t < k:
                if nums[i] <= m:
                    t += 1
                    i += 2
                else:
                    i += 1
            l, r = (m + 1, r) if t < k else (l, m)
        return l


# @leet end
sol = Solution()
nums = [2, 3, 5, 9]
k = 2

nums = [2, 7, 9, 3, 1]
k = 2

nums = [9, 6, 20, 21, 8]
k = 3
print(sol.minCapability(nums, k))
