class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        def add_zero(pos: int) -> None:
            arr.append(0)
            for j in range(len(arr) - 1, pos, -1):
                arr[j-1], arr[j] = arr[j], arr[j-1]
            del arr[-1]
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                add_zero(i)
                i += 1
            i += 1
        
        