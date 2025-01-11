from brain_games.text_data import messages
from brain_games.game_utils import (
    generate_random_number,
    convert_bool_to_yes_no,
    if_number_is_prime,
    get_user_answer,
    compare_answer,
    feedback_result
)


def brain_prime(user_name: str) -> bool:
    """
    Runs a game round where the user has to determine if a number is prime.

    Args:
        user_name (str): The name of the user playing the game.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()
    print(messages['task_prime_number'])
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    print(f"{messages['question_display']} {question_number}")
    correct_answer_bool = if_number_is_prime(question_number)
    correct_answer_str = convert_bool_to_yes_no(correct_answer_bool)
    user_answer_str = get_user_answer()
    result = compare_answer(user_answer_str, correct_answer_str)
    return feedback_result(
        result, user_name, user_answer_str, correct_answer_str
    )
