from Goals.class_goal import Goal
from datetime import date

class GrowWealthGoal(Goal):
    def __init__(self, initialContribution, monthlyContribution):
        targetYear = date.today().year + 10
        targetAmount = 1000000
        super().__init__("Grow My Wealth", targetYear, targetAmount, initialContribution, monthlyContribution)