import operator
from random import choice, randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    # messages['welcome'](user_name)
    return user_name


def victory_user(user_name):
    print(f'Congratulations, {user_name}!')


def lose_user(user_name, user_answer, correct_answer):
    print((f'"{user_answer}" is wrong answer ;(.'
           f' Correct answer was "{correct_answer}".'))
    print(f"Let's try again, {user_name}!")


def is_user_answer_correct(user_name, user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        lose_user(user_name, user_answer, correct_answer)
        return False


def generate_random_number(difficulty_level):
    random_number = randint(1, difficulty_level)
    return random_number


def if_number_is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_random_math_symbol():
    return choice(["-", "+", "*"])


def math_symbol_to_math_operation(math_symbol):
    operations = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }
    math_operation = operations[math_symbol]
    return math_operation


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

    if prime and number > 1:
        return 'yes'
    else:
        return 'no'
