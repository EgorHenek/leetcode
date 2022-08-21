class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i+len(needle) > len(haystack):
                return -1
            if "".join(haystack[i:i+len(needle)]) == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.strStr("hello", "ll") == 2
    assert solution.strStr("aaaaa", "bba") == -1
    assert solution.strStr("asdsadasdas", "") == 0
