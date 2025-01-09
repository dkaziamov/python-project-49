import prompt

from brain_games.game_utils import (
    create_arithmetic_progression,
    find_gcd,
    generate_random_math_symbol,
    generate_random_number,
    if_number_is_even,
    if_number_is_prime,
    is_user_answer_correct,
    is_user_answer_number,
    lose_user,
    math_symbol_to_math_operation,
    victory_user,
    welcome_user,
)

# v 1.0
# def start_brain_even():
#     TARGET_SCORE = 3
#     user_score = 0
#     user_name = welcome_user()
#     game_is_active = True
#     while game_is_active:
#         print('Answer "yes" if the number is even, otherwise answer "no".')
#         question_number = generate_random_number()
#         print(f'Question: {question_number}')
#         user_answer = prompt.string('Your answer: ')
#         correct_answer = if_number_is_even(question_number)
#         if user_answer == correct_answer:
#             print('Correct!')
#             user_score += 1
#             if user_score >= TARGET_SCORE:
#                 print(f'Congratulations, {user_name}!')
#                 game_is_active = False
#         else:
#             print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
#             game_is_active = False


def start_game(game_function):
    target_score = 3  # maximum score required to win the game
    difficulty_level = 10  # sets the maximum number for generate_random_number()
    user_score = 0
    user_name = welcome_user()

    while user_score < target_score:
        if not game_function(difficulty_level, user_name):
            break
        user_score += 1

    if user_score >= target_score:
        victory_user(user_name)


def brain_even(difficulty_level, user_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_number = generate_random_number(difficulty_level)
    print(f'Question: {question_number}')
    correct_answer = if_number_is_even(question_number)

    user_answer = prompt.string('Your answer: ')
    return is_user_answer_correct(user_name, user_answer, correct_answer)


def brain_calc(difficulty_level, user_name):
    print('What is the result of the expression?')
    first_number = generate_random_number(difficulty_level)
    second_number = generate_random_number(difficulty_level)
    math_symbol = generate_random_math_symbol()
    print(f'Question: {first_number} {math_symbol} {second_number}')
    correct_answer = math_symbol_to_math_operation(math_symbol)(first_number, second_number)

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)


def brain_gcd(difficulty_level, user_name):
    print('Find the greatest common divisor of given numbers.')
    first_number = generate_random_number(difficulty_level)
    second_number = generate_random_number(difficulty_level)
    print(f'Question: {first_number} {second_number}')
    correct_answer = find_gcd(first_number, second_number)

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)


def brain_progression(difficulty_level, user_name):
    print('What number is missing in the progression?')
    correct_answer = create_arithmetic_progression(difficulty_level)

    user_answer = prompt.string('Your answer: ')
    if not is_user_answer_number(user_answer):
        lose_user(user_name, user_answer, correct_answer)
        return False
    user_answer = int(user_answer)
    return is_user_answer_correct(user_name, user_answer, correct_answer)


def brain_prime(difficulty_level, user_name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question_number = generate_random_number(difficulty_level)
    print(f'Question: {question_number}')
    correct_answer = if_number_is_prime(question_number)

    user_answer = prompt.string('Your answer: ')
    return is_user_answer_correct(user_name, user_answer, correct_answer)
