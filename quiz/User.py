from datetime import datetime


class User:

    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.score = 0

    def save_score(self):
        with open('quiz/scoreboard.txt', 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, '
                       f'{self.user_name}, {self.score}\n')
