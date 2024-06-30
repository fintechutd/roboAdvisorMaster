from Goals.class_savings_goal import SavingsGoal

class TravelGoal(SavingsGoal):
    def __init__(self, destination, tripDate, tripDuration, budget, initialContribution, monthlyContribution):
        super().__init__(destination, tripDate, budget, initialContribution, monthlyContribution)
        self.tripDuration = tripDuration
        