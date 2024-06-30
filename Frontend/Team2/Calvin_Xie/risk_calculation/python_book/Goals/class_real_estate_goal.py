from Goals.class_goal import Goal
from datetime import date

class RealEstateGoal(Goal):
    def __init__(self, name, targetYear, homeValue, downPayment, mortgagePayment, interestRate):
        targetValue = downPayment
        super().__init__(name, targetYear, targetValue)
        self.homeValue = homeValue
        self.downPayment = downPayment
        self.mortgagePayment = mortgagePayment
        self.interestRate = interestRate