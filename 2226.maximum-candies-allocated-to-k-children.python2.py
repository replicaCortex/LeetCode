# @leet start
class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """

        if sum(candies) < k:
            return 0

        left = 1  # Минимальное возможное количество конфет на ребенка
        right = max(candies)  # Максимальное возможное количество конфет на ребенка
        result = 0

        while left <= right:
            mid = (left + right) // 2  # Используем бинарный поиск
            total_children = 0
            for pile in candies:
                total_children += pile // mid

            if total_children >= k:
                # Можем дать mid конфет каждому из k детей.
                # Пробуем увеличить количество конфет.
                result = mid
                left = mid + 1
            else:
                # Не можем дать mid конфет каждому из k детей.
                # Уменьшаем количество конфет.
                right = mid - 1

        return result


# @leet end
sol = Solution()
candies = [5, 8, 6]
k = 3

candies = [5, 6, 4, 10, 10, 1, 1, 2, 2, 2]
k = 9
print(sol.maximumCandies(candies, k))
