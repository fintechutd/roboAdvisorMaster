from class_risk import RiskQuestion, RiskQuestionAnswer, RiskQuestionnaire

# Page 76

# Risk tolerance
toleranceQuestionnaire = RiskQuestionnaire()

# Question 1
question1 = RiskQuestion("In general, how would your best friend describe you as a risk taker?", 2)
question1.answers.append(RiskQuestionAnswer("A real gambler", 4))
question1.answers.append(RiskQuestionAnswer("Willing to take risks after completing adequate research", 3))
question1.answers.append(RiskQuestionAnswer("Cautious", 2))
question1.answers.append(RiskQuestionAnswer("A real risk avoider", 1))

# Question 2
question2 = RiskQuestion("You are on a TV game show and can choose one of the following. Which would you take?")
question2.answers.append(RiskQuestionAnswer("A 5% chance at winning $100,000", 4))
question2.answers.append(RiskQuestionAnswer("A 25% chance at winning $10,000", 3))
question2.answers.append(RiskQuestionAnswer("A 50% chance at winning $5,000", 2))
question2.answers.append(RiskQuestionAnswer("$1,000 in cash", 1))


# Question 3
question3 = RiskQuestion("When you think of the word risk which of the following words comes to mind first?")
question3.answers.append(RiskQuestionAnswer("Thrill", 4))
question3.answers.append(RiskQuestionAnswer("Opportunity", 3))
question3.answers.append(RiskQuestionAnswer("Uncertainty", 2))
question3.answers.append(RiskQuestionAnswer("Loss", 1))

toleranceQuestionnaire.questions.append(question1)
toleranceQuestionnaire.questions.append(question2)
toleranceQuestionnaire.questions.append(question3)

# Capacity Questions page 78
capacityQuestionnaire = RiskQuestionnaire()

question4 = RiskQuestion("You are able to save money regularly.")
question4.answers.append(RiskQuestionAnswer("Completely false", 1))
question4.answers.append(RiskQuestionAnswer("Somewhat true", 2))
question4.answers.append(RiskQuestionAnswer("Completely true", 3))

question5 = RiskQuestion("You can pay all your monthly bills on time -- including any credit card or other debt.")
question5.answers.append(RiskQuestionAnswer("Completely false", 1))
question5.answers.append(RiskQuestionAnswer("Somewhat true", 2))
question5.answers.append(RiskQuestionAnswer("Completely true", 3))

question6 = RiskQuestion("If you lose money investing today, your current lifestyle would not be impacted.")
question6.answers.append(RiskQuestionAnswer("Completely false", 1))
question6.answers.append(RiskQuestionAnswer("Somewhat true", 2))
question6.answers.append(RiskQuestionAnswer("Completely true", 3))

question7 = RiskQuestion("You do not need to draw down more than 5% of your investment portfolio for any major financial goal in the next five years.")
question7.answers.append(RiskQuestionAnswer("Completely false", 1))
question7.answers.append(RiskQuestionAnswer("Somewhat true", 2))
question7.answers.append(RiskQuestionAnswer("Completely true", 3))


capacityQuestionnaire.questions.append(question4)
capacityQuestionnaire.questions.append(question5)
capacityQuestionnaire.questions.append(question6)
capacityQuestionnaire.questions.append(question7)

print("Risk Tolerance:")
toleranceQuestionnaire.answerQuestionnaire()
toleranceQuestionnaire.calculateScore()

print("Risk Capacity:")
capacityQuestionnaire.answerQuestionnaire()
capacityQuestionnaire.calculateScore()


"""
print("Risk Tolerance:")
for question in toleranceQuestionnaire.questions:
    print(question.questionText)
    for answer in question.answers:
        print("- "+answer.answerText)
    print("\n")

print("Risk Capacity:")
for question in capacityQuestionnaire.questions:
    print(question.questionText)
    for answer in question.answers:
        print("- "+answer.answerText)
    print("\n")
"""