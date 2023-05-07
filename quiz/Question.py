import json


class Question:

    questions = []

    def __init__(self, question, answers, good_answer) -> None:
        self.question = question
        self.answers = answers
        self.good_answer = good_answer

    @ staticmethod
    def load_questions():
        path = "quiz/"
        with open(path + 'questions.json', 'r', encoding='utf-8') as file:
            questions = json.load(file)
            for question in questions:
                Question.questions.append(Question(question["question"],
                                                   question["answers"],
                                                   question["good_answer"]))
