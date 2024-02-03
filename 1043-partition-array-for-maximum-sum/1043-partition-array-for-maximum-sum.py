class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)

        for j in range(k):
            dp[j] = max(arr[: j + 1]) * (j + 1)

        for j in range(k, len(arr)):
            curr = []
            for m in range(k):
                curr.append(dp[j - m - 1] + max(arr[(j - m) : (j + 1)]) * (m + 1)) 
            dp[j] = max(curr)
        return dp[-1]
