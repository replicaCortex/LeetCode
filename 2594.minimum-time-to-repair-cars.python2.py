# @leet start
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """

        def search(left, right, ans):
            if left > right:
                return ans

            mid = (left + right) // 2
            total_cars = 0
            for rank in ranks:
                total_cars += int((mid / rank) ** 0.5)

            if total_cars >= cars:  # Время подходит
                return search(left, mid - 1, mid)  # Обновляем ans и ищем меньшее
            else:
                return search(mid + 1, right, ans)  # Увеличиваем время

        right = max(ranks) * cars * cars
        return search(0, right, right)


# @leet end

sol = Solution()
ranks = [4, 2, 3, 1]
cars = 10
print(sol.repairCars(ranks, cars))
