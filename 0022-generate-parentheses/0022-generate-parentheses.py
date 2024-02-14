class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = [[""]]
        
        for i in range(1, n + 1):
            current_level = []
            for j in range(i):
                for left in result[j]:
                    for right in result[i - j - 1]:
                        current_level.append("(" + left + ")" + right)
            result.append(current_level)
        
        return result[-1]