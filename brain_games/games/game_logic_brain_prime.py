from brain_games.game_engine import play_round
from brain_games.game_utils import generate_random_number

DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()


def check_if_number_is_prime(input_number: int) -> bool:
    prime = True
    i = 2
    while i * i <= input_number:
        if input_number % i == 0:
            prime = False
            break
        i += 1
    return prime and input_number > 1


def brain_prime():
    task_message = \
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    correct_answer = \
        'yes' if check_if_number_is_prime(question_number) else 'no'
    return play_round(
        task_message=task_message,
        task_question=question_number,
        correct_answer=correct_answer,
    )
