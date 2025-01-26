# @leet start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Создаем новый связанный список для результата
        dummy = ListNode(-1)
        current = dummy

        # Пока оба списка не пусты
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Присоединяем оставшуюся часть одного из списков
        current.next = list1 if list1 else list2

        # Возвращаем результат, пропуская "dummy" узел
        return dummy.next


# @leet end


def list_to_linked_list(lst):
    """Преобразует список Python в связанный список."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(node):
    """Преобразует связанный список в список Python."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Тесты
def run_tests():
    sol = Solution()

    # Тест 1: Оба списка пустые
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    result = sol.mergeTwoLists(list1, list2)
    print("Test 1:", linked_list_to_list(result))  # Ожидаемый результат: []

    # Тест 2: Один список пустой, другой непустой
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result = sol.mergeTwoLists(list1, list2)
    print("Test 2:", linked_list_to_list(result))  # Ожидаемый результат: [0]

    # Тест 3: Оба списка содержат элементы
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    result = sol.mergeTwoLists(list1, list2)
    print(
        "Test 3:", linked_list_to_list(result)
    )  # Ожидаемый результат: [1, 1, 2, 3, 4, 4]

    # Тест 4: Одинаковые элементы в списках
    list1 = list_to_linked_list([2, 2, 2])
    list2 = list_to_linked_list([2, 2])
    result = sol.mergeTwoLists(list1, list2)
    print(
        "Test 4:", linked_list_to_list(result)
    )  # Ожидаемый результат: [2, 2, 2, 2, 2]

    # Тест 5: Один список длиннее другого
    list1 = list_to_linked_list([1, 2, 4, 5])
    list2 = list_to_linked_list([1, 3])
    result = sol.mergeTwoLists(list1, list2)
    print(
        "Test 5:", linked_list_to_list(result)
    )  # Ожидаемый результат: [1, 1, 2, 3, 4, 5]

    # Тест 6: Оба списка уже отсортированы
    list1 = list_to_linked_list([1, 3, 5])
    list2 = list_to_linked_list([2, 4, 6])
    result = sol.mergeTwoLists(list1, list2)
    print(
        "Test 6:", linked_list_to_list(result)
    )  # Ожидаемый результат: [1, 2, 3, 4, 5, 6]


# Запуск тестов
run_tests()
