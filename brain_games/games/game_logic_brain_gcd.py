from brain_games.game_utils import generate_random_number

DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()


def find_gcd(first_num: int, second_num: int) -> int:
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    return first_num + second_num


def brain_gcd():
    task_message = 'Find the greatest common divisor of given numbers.'
    first_num = generate_random_number(DIFFICULTY_LEVEL)
    second_num = generate_random_number(DIFFICULTY_LEVEL)
    task_question = f"{first_num} {second_num}"
    correct_answer = str(find_gcd(first_num, second_num))
    return task_message, task_question, correct_answer
