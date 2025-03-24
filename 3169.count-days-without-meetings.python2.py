# @leet start
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """

        # Сортируем встречи по начальной дате
        meetings.sort(key=lambda x: x[0])

        # Объединяем пересекающиеся интервалы
        merged = []
        for meeting in meetings:
            if not merged or merged[-1][1] < meeting[0]:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])

        # Подсчитываем общее количество занятых дней
        busy_days = sum(end - start + 1 for start, end in merged)

        # Возвращаем свободные дни
        return days - busy_days


# @leet end

sol = Solution()


def test_meeting_1():
    days = 5
    meetings = [[2, 4], [1, 3], [2, 5]]
    return sol.countDays(days, meetings)
    # assert sol.countDays(days, meetings) == 1


def test_meeting_2():
    days = 6
    meetings = [[1, 6]]

    assert sol.countDays(days, meetings) == 0


test_meeting_1()
test_meeting_2()
