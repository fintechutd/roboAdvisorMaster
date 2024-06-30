class RiskAssessment:
    def __init__(self):
        self.questions = [
            {'question_id': 1, 'question_text': 'In general, how would your best friend describe you as a risk taker?', 'weight': 1, 'options': ['A real gambler', 'Willing to take risks after completing adequate research', 'Cautious','A real risk avoider']},
            {'question_id': 2, 'question_text': 'You are on a TV game show and can choose one of the following. Which would you take?', 'weight': 1, 'options': ['$1,000 in cash', 'A 50% chance at winning $5,000', 'A 25% chance at winning $10,000', 'A 5% chance at winning $100,000']},
            {'question_id': 3, 'question_text': 'When you think of the word risk which of the following words comes to mind first?', 'weight': 1, 'options': ['Loss', 'Uncertainty', 'Opportunitygrowth']},
            {'question_id': 4, 'question_text': 'You are able to save money regularly.', 'weight': 1, 'options': ['Completely false', 'Somewhat true', 'Completely true']},
            {'question_id': 5, 'question_text': 'You can pay all your monthly bills on time -- including any credit card or other debt.', 'weight': 1, 'options': ['Completely false', 'Somewhat true', 'Completely true']},
            {'question_id': 6, 'question_text': 'If you lose money investing today, your current lifestyle would not be impacted.', 'weight': 1, 'options': ['Completely false', 'Somewhat true', 'Completely true']},
            {'question_id': 7, 'question_text': 'You do not need to draw down more than 5% of your investment portfolio for any major financial goal in the next five years.', 'weight': 1, 'options': ['Completely false', 'Somewhat true', 'Completely true']},
        ]
        self.answers = []
        self.risk_profile = {}

    def take_questionnaire(self):
        print("Please answer the following questions:")
        for i,question in enumerate(self.questions):
            print(f"{i+1}. {question['question_text']}")
            for i, option in enumerate(question['options'], start=1):
                print(f"  {i}. {option}")
            answer = int(input(f"Enter the number of your choice for question {question['question_id']}: "))
            # Store answer
            self.answers.append({
                'Id': len(self.answers) + 1,
                'question_id': question['question_id'],
                'Score': answer,
                'answer_text': question['options'][answer - 1]
            })

    def calculate_risk_score(self):

        # Scaler
        def scaler(value, leftMin=1, leftMax=3, rightMin=5, rightMax=55):
          # Figure out how span of each range
          leftSpan = leftMax - leftMin
          rightSpan = rightMax - rightMin

          # Convert the left range into a 0-1 range (float)
          valueScaled = float(value - leftMin) / float(leftSpan)

          # Convert the 0-1 range into a value in the right range.
          return round(rightMin + (valueScaled * rightSpan), 3)

        total_score = scaler(sum(answer['Score'] for answer in self.answers)/len(self.answers))
        self.risk_profile = {
            'client_id': 1,  # Example client ID
            'risk_tolerance': 'TBD',  # Placeholder for risk tolerance
            'risk_capacity': 'TBD',  # Placeholder for risk capacity
            'risk_score': total_score,
            'risk_id': 1  # Example risk ID
        }
        print(f"Your risk score is: {total_score}")

    def get_risk_profile(self):
        return self.risk_profile