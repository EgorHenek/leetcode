class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n == len(original):
            row = 0
            while row < m:
                original[row:row+n] = [original[row:row+n]]
                row += 1
            return original
        return []