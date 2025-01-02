# @leet start
class Solution:
    def findTheDifference(self, s, t):
        sum_s = 0
        sum_t = 0
        for i in range(len(s)):
            sum_s += ord(s[i])
        for i in range(len(t)):
            sum_t += ord(t[i])

        return chr(sum_t - sum_s)


# @leet end


# solid = Solution()
# s = "a"
# t = "aa"
# print(solid.findTheDifference(s, t))
#
# s = "abcd"
# t = "abcde"
# print(solid.findTheDifference(s, t))

# s = ""
# t = "u"
# print(solid.findTheDifference(s, t))
