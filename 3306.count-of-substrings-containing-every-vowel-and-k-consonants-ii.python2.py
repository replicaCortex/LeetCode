# @leet start
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """

        # vowels = set("aeiou")
        # result = 0
        # n = len(word)
        #
        # for start in range(n):
        #     for end in range(start + 5, n + 1):
        #         subword = word[start:end]
        #         found_vowels = set()
        #         consonant_count = 0
        #
        #         for char in subword:
        #             if char in vowels:
        #                 found_vowels.add(char)
        #             else:
        #                 consonant_count += 1
        #
        #         if len(found_vowels) == 5 and consonant_count == k:
        #             result += 1
        #
        # return result

        frequencies = [{}, {}]
        for v in "aeiou":
            frequencies[0][v] = 1

        response, currentK, vowels, extraLeft, left = 0, 0, 0, 0, 0

        for right, rightChar in enumerate(word):
            if rightChar in frequencies[0]:
                frequencies[1][rightChar] = frequencies[1].get(rightChar, 0) + 1
                if frequencies[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1

            while currentK > k:
                leftChar = word[left]
                if leftChar in frequencies[0]:
                    frequencies[1][leftChar] -= 1
                    if frequencies[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0

            while (
                vowels == 5
                and currentK == k
                and left < right
                and word[left] in frequencies[0]
                and frequencies[1][word[left]] > 1
            ):
                extraLeft += 1
                frequencies[1][word[left]] -= 1
                left += 1

            if currentK == k and vowels == 5:
                response += 1 + extraLeft

        return response


# @leet end

sol = Solution()
word = "ieaouqqieaouqq"
k = 1

word = "aeiou"
k = 0

word = "iqeaouqi"
k = 2
print(sol.countOfSubstrings(word, k))
