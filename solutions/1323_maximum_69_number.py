class Solution:
    def maximum69Number(self, num: int) -> int:
        int_list = []
        while num > 0:
            int_list.append(num % 10)
            num //= 10

        result = 0
        changed = False
        for i in range(len(int_list) - 1, -1, -1):
            if int_list[i] == 6 and not changed:
                int_list[i] = 9
                changed = True
            result += int_list[i] * (10 ** i)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum69Number(9669) == 9969
    assert solution.maximum69Number(9996) == 9999
    assert solution.maximum69Number(9999) == 9999
