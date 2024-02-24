class Solution:
    def replaceDigits(self, s: str) -> str:
        letters = string.ascii_lowercase
        result = []
        for i in range(1, len(s), 2):
            letter_index = letters.index(s[i-1])
            result.append(s[i-1])
            result.append(letters[letter_index + int(s[i])])
        if len(s) % 2:
            result.append(s[-1])
        return "".join(result)