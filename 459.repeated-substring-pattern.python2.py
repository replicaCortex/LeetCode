# @leet start


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        tmp = []
        for i in range(len(s) - 1):
            tmp.append(s[0 : i + 1])

        for k in range(len(tmp)):
            for j in range(0, len(s), len(tmp[k])):
                if (s[j : len(tmp[k]) + j]) == tmp[k]:
                    # print(s[j : len(tmp[k]) + j])
                    pass
                else:
                    tmp[k] = 0
                    break

        for p in range(len(tmp)):
            if tmp[p] != 0:
                return True

        return False


# sol = Solution()
#
# s = "abab"
#
# s = "aba"
#
# s = "abcabcabcabc"
#
#
# print(sol.repeatedSubstringPattern(s))
# @leet end
