class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        cnt = 0
        while mainTank > 0:
            cnt += 1
            if cnt % 5 == 0 and cnt > 0 and additionalTank > 0:
                mainTank += 1
                additionalTank-= 1
            mainTank -= 1
            result += 10
        return result