import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100

def is_prime(number):
    
    if number < 2:
        return False  # 1 и меньше не простые

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Нашли делитель, значит, не простое

    return True  # Делителей не нашлось, значит, простое

def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)  # число в строку для вывода
    correct_answer = "yes" if is_prime(number) else "no"  # Вызываем is_prime
    return question, correct_answer