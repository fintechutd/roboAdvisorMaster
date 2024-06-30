from datetime import date

class IncomeGoal:
    def __init__(self, durationYeras, startingValue, monthlyDividend):
        self.durationYears = durationYears
        self.startingValue = startingValue
        self.monthlyDividend = monthlyDividend

class RetirementIncome(IncomeGoal):
    def __init__(self, retirementSavings, currentAge, retirementAge, retirementIncome):
        lifeExpectancy = 79
        durationYears = lifeExpectancy-retirementAge
        super().__init__(durationYears, retirementSavings, retirementIncome)
        self.retirementYear = date.today().year + (retirementAge-currentAge)