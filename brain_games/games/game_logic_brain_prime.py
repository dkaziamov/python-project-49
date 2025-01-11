from brain_games.text_data import messages
from brain_games.game_utils import (
    generate_random_number,
    if_number_is_prime,
    feedback_result,
    ask_user_answer,
    is_user_answer_correct,
    convert_yes_no_to_bool,
    convert_bool_to_yes_no
)


def brain_prime(user_name):
    DIFFICULTY_LEVEL = 10  # sets the max number for generate_random_number()
    print(messages['task_prime_number'])
    question_number = generate_random_number(DIFFICULTY_LEVEL)
    print(f"{messages['question_display']} {question_number}")
    correct_answer_bool = if_number_is_prime(question_number)
    correct_answer_str = convert_bool_to_yes_no(correct_answer_bool)
    user_answer_str = ask_user_answer()
    user_answer_bool = convert_yes_no_to_bool(user_answer_str)
    result = is_user_answer_correct(user_answer_bool, correct_answer_bool)
    return feedback_result(result, user_name, user_answer_str, correct_answer_str)
