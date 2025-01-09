# @leet start
class Solution(object):
    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     count = 0
    #     flag = False
    #     for i in range(1, len(s) + 1):
    #         if flag != True and s[-i] != " ":
    #             count += 1
    #             flag = True
    #
    #         elif flag == True and s[-i] == " ":
    #             break
    #
    #         elif flag == True:
    #             count += 1
    #
    #         else:
    #             pass
    #
    #     return count

    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])


# @leet end

sol = Solution()
s = "Hello World"
# s = "fwef  "
# s = " f "
# s = "f"

print(sol.lengthOfLastWord(s))
