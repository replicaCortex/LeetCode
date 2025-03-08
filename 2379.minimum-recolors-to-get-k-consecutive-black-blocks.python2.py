# @leet start
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        black_count = 0
        ans = float("inf")
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == "B":
                black_count -= 1
            if blocks[i] == "B":
                black_count += 1
            ans = min(ans, k - black_count)

        return ans


# @leet end
sol = Solution()
blocks = "BWBWW"
blocks = "WBBWWBBWBW"
k = 7
print(sol.minimumRecolors(blocks, k))
