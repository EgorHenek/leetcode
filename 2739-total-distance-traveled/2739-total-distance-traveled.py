class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        while mainTank > 0:
            if mainTank >= 5:
                mainTank -= 5
                result += 50
                if additionalTank >= 1:
                    additionalTank -= 1
                    mainTank += 1
            if mainTank < 5:
                result += mainTank * 10
                mainTank = 0
        return result