# @leet start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = list(a)[::-1]
        b = list(b)[::-1]

        if len(a) < len(b):
            a, b = b, a

        for i in range(len(b)):
            if a[i] == "1" and b[i] == "1":
                a[i] = "0"
                j = 1

                while j + i - 1 < len(a):

                    if j + i == len(a):
                        a.append("1")
                        break

                    elif a[i + j] == "1":
                        a[i + j] = "0"
                        j += 1

                    elif a[i + j] == "0":
                        a[i + j] = "1"
                        j += 1
                        break

            elif a[i] == "0" and b[i] == "1":
                a[i] = "1"

        return "".join(a)[::-1]


sol = Solution()

# a = "11"
# b = "1"
# a = "1010"
# b = "1011"
a = "111"
b = "110000"
print(sol.addBinary(a, b))


# @leet end
