# @leet start
class Solution(object):
    def fib(self, n, mem={}):
        """
        :type n: int
        :rtype: int
        """
        if n in mem:
            return mem[n]

        if n <= 1:
            return n

        else:
            result = self.fib(n - 1, mem) + self.fib(n - 2, mem)
            mem[n] = result

        return result


# @leet end
sol = Solution()
n = 6
print(sol.fib(n))
