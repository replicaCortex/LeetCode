# @leet start
class Solution(object):
    def tribonacci(self, n, mem={}):
        """
        :type n: int
        :rtype: int
        """
        if n in mem:
            return mem[n]

        elif n <= 1:
            return n

        elif n == 2:
            return 1

        else:
            result = (
                self.tribonacci(n - 3, mem)
                + self.tribonacci(n - 2, mem)
                + self.tribonacci(n - 1, mem)
            )
            mem[n] = result

        return result


# @leet end

sol = Solution()


n = 3
assert (sol.tribonacci(n)) == 2
