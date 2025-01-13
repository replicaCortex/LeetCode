# @leet start
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        _tmp = []
        for i in range(len(accounts)):
            tmp = 0
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            _tmp.append(tmp)

        return max(_tmp)


# @leet end

sol = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(sol.maximumWealth(accounts))
