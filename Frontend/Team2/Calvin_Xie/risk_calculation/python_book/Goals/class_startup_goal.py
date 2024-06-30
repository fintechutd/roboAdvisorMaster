from Goals.class_goal import Goal
from datetime import date

class StartupGoal(Goal):
    def __init__(self, companyName, startYear, seedFunding):
        super().__init__(companyName, startYear, seedFunding)