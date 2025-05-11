import random

GAME_RULE = 'What is the result of the expression?'  

OPERATORS = ['+', '-', '*']  

MIN_NUMBER = 1
MAX_NUMBER = 50

def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)  
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)

    question = f'{num1} {operator} {num2}'

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2

    return question, str(correct_answer)      