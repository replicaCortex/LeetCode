# @leet start
class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return -1

        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        dominant = candidate

        total_dominant_count = 0
        for num in nums:
            if num == dominant:
                total_dominant_count += 1

        if total_dominant_count <= n / 2:
            return -1

        left_dominant_count = 0
        for i in range(1, n):
            if nums[i - 1] == dominant:
                left_dominant_count += 1

            len_left = i
            len_right = n - i
            right_dominant_count = total_dominant_count - left_dominant_count

            if len_left > 0 and len_right > 0:
                if (
                    left_dominant_count * 2 > len_left
                    and right_dominant_count * 2 > len_right
                ):
                    return i - 1

        return -1


# @leet end

sol = Solution()
nums = [1, 2, 2, 2]
nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
print(sol.minimumIndex(nums))
