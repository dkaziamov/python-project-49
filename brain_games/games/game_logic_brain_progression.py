from brain_games.text_data import messages
from brain_games.game_utils import (
    find_arithmetic_progression_answer_position,
    create_arithmetic_progression_list,
    arithmetic_progression_str,
    try_convert_to_int,
    get_user_answer,
    feedback_result,
    compare_answer
)


def brain_progression(user_name: str) -> bool:
    """
    Runs a game round where the user has to find the missing number in an
    arithmetic progression.

    Args:
        user_name (str): The name of the user playing the game.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    print(messages['task_missing_number'])
    arithmetic_progression = create_arithmetic_progression_list()
    answer_position = find_arithmetic_progression_answer_position(
        arithmetic_progression
    )
    correct_answer_int = arithmetic_progression[answer_position]
    question_line = arithmetic_progression_str(
        arithmetic_progression, answer_position
    )
    print(f"{messages['question_display']} {question_line}")
    user_answer_int = try_convert_to_int(get_user_answer())
    result = compare_answer(user_answer_int, correct_answer_int)
    return feedback_result(
        result, user_name, user_answer_int, correct_answer_int
    )
