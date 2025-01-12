import prompt
import operator

from typing import Any, Union
from brain_games.text_data import messages
from random import choice, randint


def try_convert_to_int(input_value: Any) -> Union[int, Any]:
    """
    Attempts to convert the given input to an integer.

    If the conversion fails (e.g., the input is not a valid integer),
    the original input is returned.

    Args:
        input_value (Any): The value to attempt to convert.

    Returns:
        Union[int, Any]: The integer representation of the input if successful,
        otherwise the original input.
    """
    try:
        input_value = int(input_value)
        return int(input_value)
    except ValueError:
        return input_value


def generate_random_number(DIFFICULTY_LEVEL: int) -> int:
    """
    Generates a random number between 1 and the given DIFFICULTY_LEVEL.

    Args:
        DIFFICULTY_LEVEL (int): The upper limit for the random number generation.

    Returns:
        int: A randomly generated number between 1 and DIFFICULTY_LEVEL.
    """
    return randint(1, DIFFICULTY_LEVEL)


def generate_random_math_symbol() -> str:
    """
    Generates a random mathematical symbol.

    Returns:
        str: A randomly selected math symbol ("-", "+", or "*").
    """
    return choice(["-", "+", "*"])


def math_symbol_to_math_operation(math_symbol: str) -> callable:
    """
    Converts a mathematical symbol to its corresponding operation.

    Args:
        math_symbol (str): A mathematical symbol ("-", "+", or "*").

    Returns:
        callable: The corresponding mathematical operation.
    """
    operations = {
        "-": operator.sub,
        "+": operator.add,
        "*": operator.mul,
    }
    return operations[math_symbol]


def find_gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor (GCD) of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def create_arithmetic_progression_list() -> list:
    """
    Creates a list of numbers forming an arithmetic progression.

    Returns:
        list: A list of numbers in arithmetic progression.
    """
    progression_length = randint(5, 10)
    progression_first_num = randint(1, 100)
    step = randint(2, 10)
    arithmetic_progression_list = []
    for position in range(progression_length):
        arithmetic_progression_list.append(progression_first_num)
        progression_first_num += step
    return arithmetic_progression_list


def find_arithmetic_progression_answer_position(
        arithmetic_progression_list: list) -> int:
    """
    Finds a random position in the arithmetic progression list.

    Args:
        arithmetic_progression_list (list): The list of
                                        numbers in arithmetic progression.

    Returns:
        int: A random index within the list.
    """
    answer_position = randint(0, len(arithmetic_progression_list) - 1)
    return answer_position


def arithmetic_progression_str(
        arithmetic_progression_list: list, answer_position: int) -> str:
    """
    Converts the arithmetic progression list to a string, hiding the number at
    the answer position.

    Args:
        arithmetic_progression_list (list): The list of numbers
                                            in arithmetic progression.
        answer_position (int): The index of the number to hide.

    Returns:
        str: The arithmetic progression as a string, with the hidden number.
    """
    arithmetic_progression_list[answer_position] = '..'
    arithmetic_progression_question_line = ''
    for number in arithmetic_progression_list:
        arithmetic_progression_question_line += str(number)
        arithmetic_progression_question_line += ' '
    return arithmetic_progression_question_line
