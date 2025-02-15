# @leet start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        def Search(letters=letters, target=target, right=len(letters) - 1, left=0):

            if target >= letters[-1] or target < letters[0]:
                return letters[0]

            middle = (right + left) // 2

            if right < left:
                return letters[left]

            elif ord(letters[middle]) > ord(target):
                return Search(right=middle - 1, left=left)

            elif ord(letters[middle]) <= ord(target):
                return Search(right=right, left=middle + 1)

        return Search()


# @leet end
sol = Solution()
# letters = ["c", "f", "j"]
# target = "a"

letters = ["c", "f", "j"]
target = "c"

# letters = ["c", "f", "j"]
# target = "d"
print(sol.nextGreatestLetter(letters, target))
