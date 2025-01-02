# @leet start
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        counter = {}

        for i in s:
            counter[i] = counter.get(i, 0) + 1

        for j in t:
            if j not in counter or counter[j] == 0:
                return False
            counter[j] -= 1

        return True


sol = Solution()
# s = "ggii"
# t = "eekk"

# s = "anagtam"
# t = "nbgbram"

s = "acacbac"
t = "bbbbbac"

# s = "abbba"
# t = "ababb"
print(sol.isAnagram(s=s, t=t))
# @leet end
