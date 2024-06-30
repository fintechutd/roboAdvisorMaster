from datetime import date
from dateutil import parser
from dateutil.relativedelta import relativedelta

class SavingsGoal:
    def __init__(self, name, targetDate, targetValue, initialContribution, monthlyContribution):
        targetDateTime = parser.parse(targetDate)
        delta = relativedelta(targetDateTime, date.today())
        difference_in_months = delta.months + delta.years*12
        value = initialContribution + (monthlyContribution*difference_in_months)
        print(f"Savings Goal Value: {value}")
        if not (value >= targetValue):
            raise ValueError('Target value too high to be achieved.')
        self.name = name
        self.targetDate = targetDate
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution

        #print(f"name: {self.name}")