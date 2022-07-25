class Solution:
    symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        for i, v in enumerate(s):
            if i != len(s) - 1:
                if v == 'I' and s[i+1] in ['V', 'X']:
                    result -= self.symbols[v] * 2
                elif v == 'X' and s[i+1] in ['L', 'C']:
                    result -= self.symbols[v] * 2
                elif v == 'C' and s[i+1] in ['D', 'M']:
                    result -= self.symbols[v] * 2
            result += self.symbols[v]
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
