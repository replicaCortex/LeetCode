# @leet start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        result = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result


# @leet end

sol = Solution()
s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))
