import json
from string import ascii_lowercase
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
    
    def show_question(self) -> str:
        print('\n', end='')
        print(self)
        for letter, answer in zip(ascii_lowercase, self.answers):
            print(f'{letter}. {answer}')
        print('\n', end='')

    def check_answer(self, user_answer) -> bool:
        if user_answer.lower() == self.good_answer:
            return True
        else:
            return False

    @ staticmethod
    def draw():
        unused_questions = [q for q in Question.questions if not q.used]
        number_of_unused_questions = len(unused_questions)
        if number_of_unused_questions > 0:
            random_idx = randint(0, number_of_unused_questions - 1)
            draw_question = unused_questions[random_idx]
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
