from brain_games.text_data import messages
from brain_games.game_utils import (
    generate_random_number,
    try_convert_to_int,
    get_user_answer,
    feedback_result,
    compare_answer,
    find_gcd
)


def brain_gcd(user_name: str) -> bool:
    """
    Runs a game round where the user has to find the
    greatest common divisor (GCD) of two numbers.

    Args:
        user_name (str): The name of the user playing the game.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()
    print(messages['task_gcd'])
    first_num = generate_random_number(DIFFICULTY_LEVEL)
    second_num = generate_random_number(DIFFICULTY_LEVEL)
    print(f"{messages['question_display']} {first_num} {second_num}")
    correct_answer_int = find_gcd(first_num, second_num)
    user_answer_int = try_convert_to_int(get_user_answer())
    result = compare_answer(user_answer_int, correct_answer_int)
    return feedback_result(
        result, user_name, user_answer_int, correct_answer_int
    )
