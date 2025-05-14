import random

GAME_RULE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10  # Рекомендуемая длина прогрессии
MIN_START_NUM = 1
MAX_START_NUM = 20
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def generate_round():
    start = random.randint(MIN_START_NUM, MAX_START_NUM)
    step = random.randint(MIN_STEP, MAX_STEP)
    
    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    
    progression_with_gap = []
    for i, num in enumerate(progression):
        if i == hidden_index:
            progression_with_gap.append('..')
        else:
            progression_with_gap.append(str(num))
            
    question = ' '.join(progression_with_gap)
    
    return question, correct_answer