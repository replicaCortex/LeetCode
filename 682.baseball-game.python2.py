# @leet start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        i = -1
        while True:
            i += 1

            if i == len(operations):
                return sum(operations)

            if operations[i] == "C":
                del operations[i]
                del operations[i - 1]
                i -= 2

            elif operations[i] == "D":
                del operations[i]
                operations.insert(i, 2 * operations[i - 1])

            elif operations[i] == "+":
                operations.insert(i, operations[i - 2] + operations[i - 1])
                del operations[i + 1]

            else:
                operations[i] = int(operations[i])


# @leet end

sol = Solution()
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print(sol.calPoints(ops))
