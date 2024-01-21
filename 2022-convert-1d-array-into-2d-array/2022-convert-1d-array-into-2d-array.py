class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n == len(original):
            result = []
            offset = 0
            while offset < len(original):
                result.extend([original[offset:offset+n]])
                offset += n
            return result
        return []