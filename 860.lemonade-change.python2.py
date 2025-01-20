# @leet start


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        if bills[0] != 5:
            return False

        change = []
        for i in range(len(bills)):
            if bills[i] == 5:
                change.append(5)
                bills[i] = 0

            elif bills[i] == 10:
                if 5 in change:
                    change.remove(5)
                    change.append(10)
                    bills[i] = 0

            elif bills[i] == 20:

                if 5 in change and 10 in change:
                    change.remove(5)
                    change.remove(10)
                    bills[i] = 0

                elif change.count(5) >= 3:
                    for _ in range(3):
                        change.remove(5)
                    bills[i] = 0

        return True if sum(bills) == 0 else False


# @leet end

sil = Solution()

bills = [5, 5, 5, 10, 20]
bills = [5, 5, 5, 10, 5, 20, 5, 10, 5, 20]
bills = [5, 5, 5, 20, 5, 5, 5, 20, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]

print(sil.lemonadeChange(bills))
