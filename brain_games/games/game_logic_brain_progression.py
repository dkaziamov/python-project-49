from random import randint


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


def convert_arithmetic_progression_to_str(
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


def brain_progression():
    task_message = 'What number is missing in the progression?'
    arithmetic_progression = create_arithmetic_progression_list()
    answer_position = find_arithmetic_progression_answer_position(
        arithmetic_progression
    )
    correct_answer = str(arithmetic_progression[answer_position])
    question_line = convert_arithmetic_progression_to_str(
        arithmetic_progression, answer_position
    )
    task_question = question_line
    return task_message, task_question, correct_answer
