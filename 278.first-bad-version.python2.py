# @leet start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version, bad):
#     if version == bad:
#         return True
#     else:
#         return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        first, last = 1, n

        while first < last:
            mid = first + (last - first) // 2

            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1

        return first


# @leet end
sol = Solution()
n = 100
# n = 1
print(sol.firstBadVersion(n))
