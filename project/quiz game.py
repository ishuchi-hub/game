class quiz:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
Question=[
    'quest 1: is duy khanh handsome? \nA.true \nB.false',
    'quest 2: is duy khanh the best? \nA.true \nB.false',
    'quest 3: you are nothing right?\nA.true \nB.false'
]
quizzes=[
    quiz(Question[0],'A'),
    quiz(Question[1],'A'),
    quiz(Question[2],'B')
]
def run_quizzes(quizzes):
    score=0
    for q in quizzes:
        while True:
            print(q.question)
            player=input('\033[93mA or B:\033[0m').upper()
            if player in ('A','B') :
              break

            else:
                print('\033[93mInvalid input, please choose A or B.\033[0m')
        if player==q.answer:
            score+=1
            print('correct answer')
        else:
            print('wrong answer, correct answer is:',q.answer)
        print(f'in total you have {score}/{len(Question)}')
run_quizzes(quizzes)
