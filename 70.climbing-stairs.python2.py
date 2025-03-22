# @leet start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 1

        dp = [0] * (n + 1)  # Создаем массив для хранения результатов подзадач
        dp[0] = 1  # Базовый случай
        dp[1] = 1  # Базовый случай

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Рекуррентное соотношение

        return dp[n]


# @leet end

sol = Solution()
n = 5
print(sol.climbStairs(n))
