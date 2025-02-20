# @leet start
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """

        num = "1" * len(nums[0])
        int_ = int(num, 2)
        ord_ = bin(int_)[2:]

        while len(str(bin(int_)[2:])) <= len(num):
            if ord_ not in nums:
                return ord_

            else:
                int_ -= 1
                ord_ = bin(int_)[2:]
                if ord_ == "1":
                    ord_ = "01"


# @leet end
sol = Solution()
nums = ["011", "111", "100"]

nums = ["10", "11"]
print(sol.findDifferentBinaryString(nums))
