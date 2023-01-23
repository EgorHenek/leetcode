# https://leetcode.com/problems/find-the-town-judge/
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        if len(trust) < n - 1:
            return -1
        trust_map = defaultdict(int)
        for i in trust:
            trust_map[i[0]] -= 1
            trust_map[i[1]] += 1
        for i in range(1, n + 1):
            if trust_map[i] == n - 1:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.findJudge(2, [[1, 2]]) == 2
    assert solution.findJudge(3, [[1, 3], [2, 3]]) == 3
    assert solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
    assert solution.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
