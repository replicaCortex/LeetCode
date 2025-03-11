# @leet start
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        count = {"a": 0, "b": 0, "c": 0}
        left = 0

        for right in range(n):
            if s[right] in count:
                count[s[right]] += 1

            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                result += n - right
                if s[left] in count:
                    count[s[left]] -= 1
                left += 1

        return result


# @leet end
sol = Solution()

s = "abcabc"

print(sol.numberOfSubstrings(s))
