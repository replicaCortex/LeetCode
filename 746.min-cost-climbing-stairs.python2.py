# @leet start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * (len(cost) + 2)

        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])


# @leet end

sol = Solution()

assert sol.minCostClimbingStairs(cost=[10, 15, 20]) == 15
assert sol.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
