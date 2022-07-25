class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        signs = {'(': ')', '{': '}', '[': ']'}
        for sign in s:
            if sign in signs:
                stack.append(sign)
            else:
                if len(stack) == 0 or signs[stack.pop()] != sign:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert solution.isValid("(]") is False
    assert solution.isValid("]") is False
