# @leet start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(1, len(digits) + 1):
            if digits[-i] == 9:
                digits[-i] = 0
                if len(digits) == i:
                    digits.insert(0, 1)
            else:
                digits[-i] = digits[-i] + 1
                break

        return digits


sol = Solution()
# digits = [1, 2, 3]
# digits = [9]
# digits = [1, 9]
digits = [9, 9, 9]
print(sol.plusOne(digits))
# @leet end
