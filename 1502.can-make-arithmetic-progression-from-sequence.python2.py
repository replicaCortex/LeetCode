# @leet start
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) <= 2:
            return True

        arr = sorted(arr)
        pattern = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != pattern:
                return False

        return True


sol = Solution()
arr = [3, 5, 1]
print(sol.canMakeArithmeticProgression(arr))
# @leet end
