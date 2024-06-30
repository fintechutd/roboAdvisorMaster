from Goals.class_goal import Goal
from datetime import date
class RetirementGoal(Goal):
    def __init__(self, name, targetValue, startingAge, retirementAge):
        targetYear = date.today().year + (retirementAge-startingAge)
        super().__init__(name, targetYear, targetValue)
        self.retirementAge = retirementAge