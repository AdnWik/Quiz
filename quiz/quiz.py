from Question import Question
from User import User

Question.load_questions()
score = 0

print('\n', end='')
print("Welcome in Quiz game")
while True:
    question = Question.draw()
    if question:
        question.show_question()
        user_answer = input('Your answer: ')
        if question.check_answer(user_answer):
            score += 1
            print('Good answer')
        else:
            print('Bad answer')
    else:
        print('\n', end='')
        print('Quiz finish here')
        user_name = input('Enter your name: ')
        user = User(user_name)
        user.score = score
        print(f'{user.user_name} you get '
              f'{user.score}/{len(Question.questions)} points.')
        user.save_score()
        break
