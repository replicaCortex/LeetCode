# @leet start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        sum_s, sum_t = 0, 0
        for i in range(len(s)):
            sum_s += ord(s[i])
        for i in range(len(t)):
            sum_t += ord(t[i])
        if sum_t == sum_s and (len(s) == len(t)):
            for i in range(len(s)):
                if (s[i] in t) and (t[i] in s):
                    count += 1
                    if count == len(s):
                        return True

                else:
                    return False
        else:
            return False


sol = Solution()
s = "ggii"
t = "eekk"

s = "anagtam"
t = "nbgbram"

s = "acacbac"
t = "bbbbbac"
print(sol.isAnagram(s=s, t=t))
# @leet end
