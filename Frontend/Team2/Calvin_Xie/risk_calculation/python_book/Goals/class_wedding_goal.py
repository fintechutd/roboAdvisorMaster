from Goals.class_savings_goal import SavingsGoal

class WeddingGoal(SavingsGoal):
    def __init__(self, name, weddingDate, budget, initialContribution, monthlyContribution):
        super().__init__(name, weddingDate, budget, initialContribution, monthlyContribution)
        self.weddingDate = weddingDate
        