class RiskQuestion:
    def __init__(self, questionText, weight=1):
        self.questionText = questionText
        self.weight = weight
        self.answers = []

class RiskQuestionAnswer:
    def __init__(self, answerText, score, selected = False):
        self.answerText = answerText
        self.score = score
        self.selected = selected

class RiskQuestionnaire:
    def __init__(self):
        self.questions = []

    def answerQuestionnaire(self):
        for i in range (len(self.questions)):
            question = self.questions[i]
            print(question.questionText)
            for n in range (len(question.answers)):
                answer = question.answers[n]
                print(f"{str(n)}: {answer.answerText}")
            nChosen = int(input(f"Choose your answers between 0 and {str(len(question.answers)-1)}: "))
            self.questions[i].answers[nChosen].selected = True
            print("\n")
    
    def calculateScore(self):
        print("Risk Score:")
        myTotalScore = 0
        for question in self.questions:
            for answer in question.answers:
                if(answer.selected == True):
                    myTotalScore += (answer.score*question.weight)
                    print(f"{answer.answerText}: {str(answer.score*question.weight)}")
        print(f"Total Risk Score: {myTotalScore}\n")
