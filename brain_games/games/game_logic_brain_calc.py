import operator
from random import choice

from brain_games.game_utils import generate_random_number

DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()


def convert_math_symbol_to_math_operation(math_symbol: str) -> callable:
    operations = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }
    return operations[math_symbol]


def brain_calc():
    task_message = 'What is the result of the expression?'
    first_num = generate_random_number(DIFFICULTY_LEVEL)
    second_num = generate_random_number(DIFFICULTY_LEVEL)
    math_symbol = choice(["-", "+", "*"])
    task_question = f"{first_num} {math_symbol} {second_num}"
    correct_answer = str(convert_math_symbol_to_math_operation(math_symbol)(
        first_num, second_num
    ))
    return task_message, task_question, correct_answer
