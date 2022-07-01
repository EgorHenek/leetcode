class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(121)
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(123) is False
    print('Accept')
