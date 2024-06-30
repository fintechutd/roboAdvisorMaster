class Goal:
    def __init__(self, name, targetYear, targetValue, initialContribution = 0, monthlyContribution=0, priority = ""):
        self.name = name
        self.targetYear = targetYear
        self.targetValue = targetValue
        self.initialContribution = initialContribution
        self.monthlyContribution = monthlyContribution
        if not (priority == "") and not (priority in ["Dreams", "Wishes", "Wants", "Needs"]):
            raise ValueError('Wrong value set for Priority')
        self.priority = priority
