import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer