# @leet start
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) == 2:
            return True

        arr = sorted(arr)
        count = 0
        pattern = abs(arr[0] - arr[1])
        for i in range(1, len(arr)):
            if i + 1 < len(arr) and abs(arr[i] - arr[i + 1]) == pattern:
                count += 1
                if count == len(arr) - 2:
                    return True
            else:
                return False


# sol = Solution()
# arr = [3, 5, 1]
# print(sol.canMakeArithmeticProgression(arr))
# @leet end
