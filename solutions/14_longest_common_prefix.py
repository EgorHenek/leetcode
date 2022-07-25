class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i, char in enumerate(strs[0]):
            for other_word in strs[1:]:
                if len(other_word) - 1 < i or other_word[i] != char:
                    return result
            result += char
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["ab", "a"]) == "a"
