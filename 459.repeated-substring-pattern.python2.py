# @leet start


class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False


# sol = Solution()
#
# s = "abab"
#
# s = "aba"
#
# s = "abcabcabcabc"
# #
# #
# print(sol.repeatedSubstringPattern(s))
# @leet end
