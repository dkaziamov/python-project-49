import operator

from brain_games.text_data import messages
from random import choice, randint

import prompt


def ask_user_name():
    return prompt.string('May I have your name? ')


def ask_user_answer():
    return prompt.string('Your answer: ')


def convert_yes_no_to_bool(str_value):
    return str_value == 'yes'


def convert_bool_to_yes_no(bool_value):
    if bool_value:
        return 'yes'
    return 'no'


def is_user_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def feedback_result(boolean_value, user_name, user_answer, correct_answer):
    if boolean_value:
        print(messages['feedback_correct'])
        return True
    print(messages['feedback_wrong_answer'](user_answer, correct_answer))
    print(messages['feedback_try_again'](user_name))
    return False


def generate_random_number(DIFFICULTY_LEVEL):
    return randint(1, DIFFICULTY_LEVEL)


def if_number_is_even(number):
    return number % 2 == 0


def generate_random_math_symbol():
    return choice(["-", "+", "*"])


def math_symbol_to_math_operation(math_symbol):
    operations = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }
    return operations[math_symbol]


def is_user_answer_number(user_answer):
    try:
        user_answer = int(user_answer)
        return True
    except ValueError:
        return False


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def create_arithmetic_progression(difficulty_level):
    length = randint(5, 10)
    start_number = randint(1, 100)
    step = randint(2, difficulty_level)
    list_of_numbers = []
    for position in range(length):
        list_of_numbers.append(start_number)
        start_number += step

    answer_position = randint(0, length - 1)
    answer = list_of_numbers[answer_position]
    list_of_numbers[answer_position] = '..'

    question_line = ''
    for number in list_of_numbers:
        question_line += str(number)
        question_line += ' '
    print(f'Question: {question_line}')
    return answer


def if_number_is_prime(number):
    prime = True
    i = 2
    while i * i <= number:
        if number % i == 0:
            prime = False
            break
        i += 1
    return prime and number > 1
