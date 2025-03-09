# @leet start
class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        # start_point = 0
        # for i in range(len(colors)):
        #     if colors[i] == colors[i - 1]:
        #         start_point = i
        #         break
        #
        # for _ in range(len(colors[0:start_point])):
        #     del_color = colors.pop(0)
        #     colors.append(del_color)
        #
        # start, end = 0, k
        # pattern = 0
        # while end <= len(colors):
        #     for i in range(start + 1, end):
        #         if colors[i] == colors[i - 1]:
        #             pattern -= 1
        #             break
        #
        #     pattern += 1
        #
        #     start += 1
        #     end += 1
        #
        # return pattern

        colors.extend(colors[: (k - 1)])
        count = 0
        left = 0

        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right - 1]:
                left = right

            if right - left + 1 >= k:
                count += 1

        return count


# @leet end
sol = Solution()
# colors = [0, 1, 0, 1, 0]
# k = 3

# colors = [0, 1, 0, 0, 1, 0, 1]
# k = 6

colors = [0, 1, 0, 0, 1]
k = 2
print(sol.numberOfAlternatingGroups(colors, k))
