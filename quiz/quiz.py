from Question import Question

Question.load_questions()

print("Welcome in Quiz game")
while True:
    question = Question.draw()
    if question:
        print('\n', end='')
        print("="*50)

        print(question)
        for number, answer in enumerate(question.answers, start=1):
            print(f'{number}. {answer}')
        
        print('\n', end='')
        user_answer = input('Your answer: ')
    else:
        break