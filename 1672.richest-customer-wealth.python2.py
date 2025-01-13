# @leet start
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        return max([sum(acc) for acc in accounts])


# @leet end

sol = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(sol.maximumWealth(accounts))
