# @leet start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):

            dict_t = {}
            dict_s = {}
            count = 0
            len_ = len(s)

            for i in range(len_):
                if s[i] not in dict_s:
                    dict_s[s[i]] = 1
                elif s[i] in dict_s:
                    value = dict_s[s[i]]
                    dict_s[s[i]] = value + 1

            for i in range(len_):
                if t[i] not in dict_t:
                    dict_t[t[i]] = 1
                elif t[i] in dict_t:
                    value = dict_t[t[i]]
                    dict_t[t[i]] = value + 1

            for j in range(len_):
                if s[j] in dict_t:
                    if dict_s[s[j]] == dict_t[s[j]]:
                        count += 1
                        if count == len_:
                            return True
                    else:
                        return False
                else:
                    return False

        else:
            return False


sol = Solution()
# s = "ggii"
# t = "eekk"

s = "anagtam"
t = "nbgbram"

# s = "acacbac"
# t = "bbbbbac"

# s = "abbba"
# t = "ababb"
print(sol.isAnagram(s=s, t=t))
# @leet end
