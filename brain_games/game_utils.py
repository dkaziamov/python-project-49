import prompt
import operator

from typing import Any, Union
from brain_games.text_data import messages
from random import choice, randint


def get_user_name() -> str:
    """
    Prompts the user to enter their name.

    Returns:
        str: The name entered by the user.
    """
    return prompt.string(messages['user_name'])


def get_user_answer() -> str:
    """
    Prompts the user to enter their answer.

    Returns:
        str: The answer entered by the user.
    """
    return prompt.string(messages['user_answer'])


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


def convert_bool_to_yes_no(bool_value: bool) -> str:
    """
    Converts a boolean value to a string 'yes' or 'no'.

    Args:
        bool_value (bool): The boolean value to convert.

    Returns:
        str: 'yes' if the input is True, 'no' otherwise.
    """
    if bool_value:
        return 'yes'
    return 'no'


def compare_answer(user_answer: Any, correct_answer: Any) -> bool:
    """
    Compares two values to determine if they are equal.

    Args:
        user_answer (Any): The user's answer to compare.
        correct_answer (Any): The correct answer to compare against.

    Returns:
        bool: True if the answers are equal, False otherwise.
    """
    return user_answer == correct_answer


def feedback_result(
    result: bool, user_name: str, user_answer: str, correct_answer: str
) -> bool:
    """
    Provides feedback to the user based on their answer.

    Args:
        result (bool): Whether the user's answer was correct.
        user_name (str): The name of the user providing the answer.
        user_answer (str): The answer provided by the user.
        correct_answer (str): The correct answer.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    if result:
        print(messages['feedback_correct'])
        return True
    print(messages['feedback_wrong_answer'](user_answer, correct_answer))
    print(messages['feedback_try_again'](user_name))
    return False


def generate_random_number(DIFFICULTY_LEVEL: int) -> int:
    """
    Generates a random number between 1 and the given DIFFICULTY_LEVEL.

    Args:
        DIFFICULTY_LEVEL (int): The upper limit for the random number generation.

    Returns:
        int: A randomly generated number between 1 and DIFFICULTY_LEVEL.
    """
    return randint(1, DIFFICULTY_LEVEL)


def if_number_is_even(input_number: int) -> bool:
    """
    Checks if the given number is even.

    Args:
        input_number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return input_number % 2 == 0


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


def if_number_is_prime(input_number: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        input_number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
       """
    prime = True
    i = 2
    while i * i <= input_number:
        if input_number % i == 0:
            prime = False
            break
        i += 1
    return prime and input_number > 1
