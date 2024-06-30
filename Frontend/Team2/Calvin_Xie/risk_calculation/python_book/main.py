from imports import *
from datetime import date
from dateutil.relativedelta import relativedelta


# General Goal
myGoal = Goal("Retirement", 2060, 3000000)
myGoal.initialContribution = 10000
retirementAge = 65
startingAge = 41
targetYear = date.today().year + (retirementAge-startingAge)
myGoal.targetYear = targetYear
print(f"my goal target year: {myGoal.targetYear}")


# Retirement
myRetirement = RetirementGoal("Honolulu", 300000, 41, 60)
print(f"my retirement goal target year: {myRetirement.targetYear}")


# Growth Wealth
myGrowthWealth = GrowWealthGoal(10000, 1000)
print(f"my retirement goal target year: {myGrowthWealth.targetYear}")


# Savings Goal
new_date = date.today() + relativedelta(years=1)
new_date = new_date.strftime("%B %d, %Y")
print("Savings Goal:")
saver = SavingsGoal("Rainy Day", new_date, 10000, 1000, 1000) # this does not print an error statement
#saver = SavingsGoal("Rainy Day", new_date, 10000, 1000, 100) # This prints an error statement

# Splurge Goal
new_date = date.today() + relativedelta(months=3)
new_date = new_date.strftime("%B %d, %Y")
print("Splurge Goal:")
goal = SplurgeGoal("MacBook", "Apple", new_date, 1500, 500, 500)
goal.name
goal.initialContribution

# stopped at page 70
