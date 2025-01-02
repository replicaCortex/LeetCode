# @leet start
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


# solid = Solution()
# haystack = "sadbutsad"
# needle = "tsad"
# print(solid.strStr(haystack, needle))
# #
# #
# # haystack = "hello"
# # needle = "ll"
# print(solid.strStr(haystack, needle))
# @leet end
