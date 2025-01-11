from brain_games.text_data import messages
from brain_games.game_utils import (
    math_symbol_to_math_operation,
    generate_random_math_symbol,
    generate_random_number,
    try_convert_to_int,
    get_user_answer,
    feedback_result,
    compare_answer,
)


def brain_calc(user_name: str) -> bool:
    """
    Runs a game round where the user has to solve a math expression.

    Args:
        user_name (str): The name of the user playing the game.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()
    print(messages['task_expression_result'])
    first_num = generate_random_number(DIFFICULTY_LEVEL)
    second_num = generate_random_number(DIFFICULTY_LEVEL)
    math_symbol = generate_random_math_symbol()
    print(f"{messages['question_display']} "
          f"{first_num} {math_symbol} {second_num}")
    correct_answer_int = math_symbol_to_math_operation(math_symbol)(
        first_num, second_num
    )
    user_answer_int = try_convert_to_int(get_user_answer())
    result = compare_answer(user_answer_int, correct_answer_int)
    return feedback_result(
        result, user_name, user_answer_int, correct_answer_int
    )
