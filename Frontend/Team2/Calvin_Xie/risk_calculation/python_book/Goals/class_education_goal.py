from Goals.class_goal import Goal
from datetime import date

class EducationGoal(Goal):
    def __init__(self, name, startYear, degreeLengthYears, annualTuitionFees, degreeType, schoolName):
        targetValue = degreeLengthYears*annualTuitionFees
        super().__init__(name, startYear, targetValue)
        self.degreeType = degreeType
        self.schoolName = schoolName