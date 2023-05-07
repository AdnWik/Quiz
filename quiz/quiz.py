from Question import Question

Question.load_questions()
for question in Question.questions:
    print(f'{question.question} | {question.answers} | {question.good_answer}')
