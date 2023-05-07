import json
from random import randint


class Question:

    questions = []

    def __init__(self, question, answers, good_answer) -> None:
        self.question = question
        self.answers = answers
        self.good_answer = good_answer
        self.used = False

    def __str__(self) -> str:
        return f'{self.question}'

    def play(self):
        print('\n', end='')
        print("="*50)

        print(self)
        for number, answer in enumerate(self.answers, start=1):
            print(f'{number}. {answer}')
        
        print('\n', end='')
        user_answer = int(input('Your answer: '))
        print(self.answers[user_answer])

    @ staticmethod
    def draw():
        unused_questions = [q for q in Question.questions if q.used == False]
        number_of_unused_questions = len(unused_questions)
        if number_of_unused_questions > 0:
            draw_question = unused_questions[randint(0, number_of_unused_questions - 1)]
            draw_question.used = True
            return draw_question
        else:
            return None


    @ staticmethod
    def load_questions():
        path = "quiz/"
        with open(path + 'questions.json', 'r', encoding='utf-8') as file:
            questions = json.load(file)
            for question in questions:
                Question.questions.append(Question(question["question"],
                                                   question["answers"],
                                                   question["good_answer"]))
