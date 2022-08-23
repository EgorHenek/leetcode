class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        switch = False
        for i in s[::-1]:
            if i != ' ':
                count += 1
                switch = True
            elif switch:
                break
        return count


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
