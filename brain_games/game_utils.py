import operator

from brain_games.text_data import messages
from random import choice, randint

import prompt


def get_user_name():
    return prompt.string(messages['user_name'])


def get_user_answer():
    return prompt.string(messages['user_answer'])


def try_convert_to_int(input_value):
    try:
        input_value = int(input_value)
        return int(input_value)
    except ValueError:
        return input_value


def convert_bool_to_yes_no(bool_value):
    if bool_value:
        return 'yes'
    return 'no'


def is_user_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def feedback_result(result, user_name, user_answer, correct_answer):
    if result:
        print(messages['feedback_correct'])
        return True
    print(messages['feedback_wrong_answer'](user_answer, correct_answer))
    print(messages['feedback_try_again'](user_name))
    return False


def generate_random_number(DIFFICULTY_LEVEL):
    return randint(1, DIFFICULTY_LEVEL)


def if_number_is_even(input_number):
    return input_number % 2 == 0


def generate_random_math_symbol():
    return choice(["-", "+", "*"])


def math_symbol_to_math_operation(math_symbol):
    operations = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }
    return operations[math_symbol]


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def create_arithmetic_progression(DIFFICULTY_LEVEL):
    length = randint(5, 10)
    start_number = randint(1, 100)
    step = randint(2, DIFFICULTY_LEVEL)
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


def if_number_is_prime(input_number):
    prime = True
    i = 2
    while i * i <= input_number:
        if input_number % i == 0:
            prime = False
            break
        i += 1
    return prime and input_number > 1
