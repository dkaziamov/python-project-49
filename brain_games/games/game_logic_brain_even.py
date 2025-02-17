from brain_games.game_utils import generate_random_number

DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()


def brain_even():
    task_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    correct_answer = 'yes' if question_number % 2 == 0 else 'no'
    return task_message, question_number, correct_answer
