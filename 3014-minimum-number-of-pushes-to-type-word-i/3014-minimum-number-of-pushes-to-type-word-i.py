class Solution:
    def minimumPushes(self, word: str) -> int:
        div, mod = divmod(len(word), 8)
        result = 0
        for i in range(div):
            result += (i + 1) * 8
        result += mod * (div + 1)
        return result
