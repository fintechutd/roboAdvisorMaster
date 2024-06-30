from Goals.class_savings_goal import SavingsGoal

class SplurgeGoal(SavingsGoal):
    def __init__(self, itemName, storeName, targetPurchaseDate, budget, initialContribution, monthlyContribution):
        super().__init__(itemName + " @ " + storeName, targetPurchaseDate, budget, initialContribution, monthlyContribution)
        