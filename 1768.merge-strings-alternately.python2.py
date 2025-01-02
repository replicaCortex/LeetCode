# @leet start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        len1, len2 = len(word1), len(word2)
        # Перемешиваем по очереди
        for i in range(max(len1, len2)):
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])
        return "".join(merged)


# тестирование функции mergealternately
solution = Solution()
#
# word1 = "abc"
# word2 = "pqr"
# result = solution.mergealternately(word1, word2)
# print(result)
#
# word1 = "ab"
# word2 = "pqr"
# result = solution.mergealternately(word1, word2)
# print(result)

word1 = "abcd"
word2 = "pq"

result = solution.mergeAlternately(word1, word2)
print(result)
# Ожидаемый результат

# @leet end
