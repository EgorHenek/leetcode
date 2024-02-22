class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dp = [0] * n
        for i in trust:
            dp[i[1] - 1] += 1
            dp[i[0] - 1] = -1
        try:
            return dp.index(n-1) + 1
        except ValueError:
            return -1